import os
import cPickle
from cPickle import PickleError
from abc import abstractmethod
from twitter.common import log
from twitter.common.dirutil import safe_mkdir
from collections import namedtuple
from addict import Dict
from state_manager import Clusterstate, Nodestate
from god.common.utils import *
from twitter.common.quantity import Amount, Data


class StateProvider(object):
  """
    StateProvider is responsible for checkpointing and restoring the state of the Hyaline scheduler.

    It maintains the following key hierarchy:
      /state/scheduler  # Scheduler-level state.
      /state/clusters/  # Folder for all cluster-level states.
        cluster1        # State for 'cluster1'.
        cluster2        # State for 'cluster2'.
        ...
  """

  class Error(Exception): pass

  @abstractmethod
  def dump_scheduler_state(self, state):
    """Persist scheduler-level state."""
    pass

  @abstractmethod
  def load_scheduler_state(self):
    """
      Restore scheduler-level state.
      :return: The Scheduler object. None if no state is available.
    """
    pass

  @abstractmethod
  def dump_cluster_state(self, state):
    """Persist cluster-level state."""
    pass

  @abstractmethod
  def load_cluster_state(self, cluster_name):
    """
      Restore cluster-level state.
      :return: The MySQLCluster object. None if no state is available.
    """
    pass

  @abstractmethod
  def remove_cluster_state(self, cluster_name):
    """Remove cluster-level state."""
    pass

  @abstractmethod
  def remove_mysql_state(self, cluster_name, task_id):
    """Remove cluster-level state."""
    pass

  # --- Helper methods. ---
  @classmethod
  def _get_scheduler_state_key(cls):
    return ['state', 'scheduler']

  @classmethod
  def _get_cluster_state_key(cls, cluster_name):
    return ['state', 'clusters', cluster_name]

  @classmethod
  def _get_mysql_state_key(cls, cluster_name, task_id):
    return ['state', 'clusters', cluster_name, task_id]

  @classmethod
  def _get_mysql_log_key(cls, cluster_name, task_id):
    return ['ClusterMessages', cluster_name,"mysql_log", task_id]

class Scheduler(object):
  """
    Scheduler-level state.

    NOTE: It references cluster-level states indirectly through cluster names.
  """

  def __init__(self):
    self.framework_id = None
    self.clusters = dict()
    self.release = []

class Cluster(object):
  """
    The state of a cluster.

    It includes tasks for members of the cluster.
  """

  def __init__(self,
               id,
               name,
               user,
               encrypted_password,
               num_nodes):
    if not isinstance(num_nodes, int):
      raise TypeError("'num_nodes' should be an int")

    self.cluster_id = id
    self.name = name
    self.user = user
    self.encrypted_password = encrypted_password
    self.num_nodes = num_nodes
    self.create_time = time.time()
    self.tasks = {}   # {TaskID : MySQLTask} mappings
    self.next_id = 1  # Monotonically increasing number for unique task IDs.
    self.clusterstate = Clusterstate.INITIALIZING
    self.cpus = 0.5
    self.mem = Amount(256, Data.MB)
    self.disk = Amount(512, Data.MB)

  @property
  def active_tasks(self):
    """Tasks that have been launched and have not terminated."""
    return [t for t in self.tasks.values() if t.nodestate in (Nodestate.STARTING, Nodestate.RUNNING)]

  @property
  def running_tasks(self):
    return [k for k,v in self.tasks.items() if v.state in (mesos_pb2.TASK_RUNNING,)]

  @property
  def starting_tasks(self):
    return [k for k,v in self.tasks.items() if v.state in (mesos_pb2.TASK_STARTING,)]

class Task(object):
  """The state of a MySQL task."""

  def __init__(self, cluster_name, task_id, server_id, cpus, mem, disk, mesos_slave_id=None, hostname=None, port=None, identity='slave'):

    self.cluster_name = cluster_name  # So we can refer back to the cluster it belongs to.
    self.task_id = task_id
    self.mesos_slave_id = mesos_slave_id
    self.hostname = hostname
    self.ip = None
    self.cpus = cpus
    self.mem = mem
    self.disk = disk
    self.port = port
    # self.state = mesos_pb2.TASK_STAGING  # Initial state. Will be updated by statusUpdate().
    self.nodestate=Nodestate.STAGING
    self.sandboxdir = None
    self.create_time = time.time()

  @property
  def node_info(self):
    NodeInfo = namedtuple('NodeInfo', [
      'task_id',
      'ip',
      'create_time',
      'sandboxdir',
      'cpus',
      'mem',
      'disk',
      'port',
      'state',
      'cluster_name'])
    return NodeInfo(
      task_id=self.task_id,
      ip=str(self.ip),
      create_time=gettime(self.create_time),
      sandboxdir=str(self.sandboxdir),
      cpus=self.cpus,
      mem=self.mem.as_(Data.MB),
      disk='%.2f' %self.disk.as_(Data.GB),
      port=str(self.port),
      state=self.nodestate,
      cluster_name=self.cluster_name)

class LocalStateProvider(StateProvider):
  """StateProvider implementation that uses local disk to store the state."""

  def __init__(self, work_dir):
    """
      :param work_dir: The root directory under which the scheduler state is stored. e.g. The path
                       for 'cluster1' is <work_dir>/state/clusters/cluster1.
    """
    self._work_dir = work_dir

  def dump_scheduler_state(self, state):
    if not isinstance(state, Scheduler):
      raise TypeError("'state' should be an instance of Scheduler")
    path = self._get_scheduler_state_path()
    safe_mkdir(os.path.dirname(path))

    try:
      with open(path, 'wb') as f:
        cPickle.dump(state, f)
    except PickleError as e:
      raise self.Error('Failed to persist Scheduler: %s' % e)

  def load_scheduler_state(self):
    path = self._get_scheduler_state_path()
    if not os.path.isfile(path):
      log.info("No scheduler state found on path %s" % path)
      return None

    try:
      with open(path, 'rb') as f:
        return cPickle.load(f)
    except PickleError as e:
      raise self.Error('Failed to recover Scheduler: %s' % e)

  def dump_cluster_state(self, state):
    if not isinstance(state, Cluster):
      raise TypeError("'state' should be an instance of MySQLCluster")
    path = self._get_cluster_state_path(state.name)
    safe_mkdir(os.path.dirname(path))

    try:
      with open(path, 'wb') as f:
        return cPickle.dump(state, f)
    except PickleError as e:
      raise self.Error('Failed to persist state for cluster %s: %s' % (state.name, e))

  def load_cluster_state(self, cluster_name):
    path = self._get_cluster_state_path(cluster_name)
    if not os.path.isfile(path):
      log.info("No cluster state found on path %s" % path)
      return None

    try:
      with open(path, 'rb') as f:
        return cPickle.load(f)
    except PickleError as e:
      raise self.Error('Failed to recover MySQLCluster: %s' % e)

  def remove_cluster_state(self, cluster_name):
    path = self._get_cluster_state_path(cluster_name)
    if not os.path.isfile(path):
      log.info("No cluster state found on path %s" % path)
      return

    os.remove(path)

  # --- Helper methods. ---
  def _get_scheduler_state_path(self):
    return os.path.join(self._work_dir, os.path.join(*self._get_scheduler_state_key()))

  def _get_cluster_state_path(self, cluster_name):
    return os.path.join(self._work_dir, os.path.join(*self._get_cluster_state_key(cluster_name)))

