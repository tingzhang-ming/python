# -*- coding:utf-8 -*-
import cPickle
from cPickle import PickleError
import posixpath
from twitter.common import log
from god.scheduler.state import Scheduler, StateProvider, Cluster
from kazoo.exceptions import KazooException, NoNodeError

class ZooKeeperStateProvider(StateProvider):
  """
    StateProvider implementation backed by ZooKeeper.

    This class is thread-safe.
  """

  def __init__(self, client, base_path, password_box):
    """
      :param client: Kazoo client.
      :param base_path: The base path for the scheduler state on ZooKeeper.
    """
    self._client = client
    self._base_path = base_path
    self._password_box = password_box

  #存调度器状态至zookeeper
  def dump_scheduler_state(self, state):
    if not isinstance(state, Scheduler):
      raise TypeError("'state' should be an instance of Scheduler")

    path = self._get_scheduler_state_path()
    self._client.retry(self._client.ensure_path, posixpath.dirname(path))

    content = cPickle.dumps(state)
    try:
      self._client.retry(self._create_or_set, path, content)
    except KazooException as e:
      raise self.Error('Failed to persist Scheduler: %s' % e)

  #从zookeeper上取出调度器状态
  def load_scheduler_state(self):
    path = self._get_scheduler_state_path()

    try:
      content = self._client.get(path)[0]
      state = cPickle.loads(content)
      if not isinstance(state, Scheduler):
        raise self.Error("Invalid state object. Expect Scheduler, got %s" % type(state))
      return state
    except NoNodeError:
      log.info('No scheduler state found on path %s' % path)
      return None
    except (KazooException, PickleError, ValueError) as e:
      raise self.Error('Failed to recover Scheduler: %s' % e)

  #存集群状态至zookeeper和资源回写数据库
  def dump_cluster_state(self, state):
    if not isinstance(state, Cluster):
      raise TypeError("'state' should be an instance of MySQLCluster")
    path = self._get_cluster_state_path(state.name)
    self._client.retry(self._client.ensure_path, posixpath.dirname(path))
    content = cPickle.dumps(state)
    self._client.retry(self._create_or_set, path, content)

  # 从zookeeper上取出集群状态
  def load_cluster_state(self, cluster_name):
    path = self._get_cluster_state_path(cluster_name)

    try:
      content = self._client.get(path)[0]
      state = cPickle.loads(content)
      if not isinstance(state, Cluster):
        raise self.Error("Invalid state object. Expect MySQLCluster, got %s" % type(state))
      return state
    except NoNodeError:
      log.info('No cluster state found on path %s' % path)
      return None
    except (KazooException, PickleError, ValueError) as e:
      raise self.Error('Failed to recover MySQLCluster: %s' % e)

  #从zookeeper上移除集群
  def remove_cluster_state(self, cluster_name):
    path = self._get_cluster_state_path(cluster_name)
    try:
      self._client.retry(self._client.delete, path, recursive=True)
    except KazooException as e:
      raise self.Error("Failed to remove MySQLCluster: %s" % e)

  # --- Helper methods. ---
  def _get_scheduler_state_path(self):
    return posixpath.join(self._base_path, posixpath.join(*self._get_scheduler_state_key()))

  def _get_cluster_state_path(self, cluster_name):
    return posixpath.join(
        self._base_path, posixpath.join(*self._get_cluster_state_key(cluster_name)))

  def _get_mysql_state_path(self, cluster_name, task_id):
    return posixpath.join(
        self._base_path, posixpath.join(*self._get_mysql_state_key(cluster_name, task_id)))

  def _get_mysql_log_path(self, cluster_name, task_id):
    return posixpath.join(
        self._base_path, posixpath.join(*self._get_mysql_log_key(cluster_name, task_id)))

  def _create_or_set(self, path, content):
    """Set the ZNode if the path exists, otherwise create it."""
    if self._client.exists(path):
      self._client.set(path, content)
    else:
      self._client.create(path, content)

