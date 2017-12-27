#!/usr/bin/env python2.7
from __future__ import print_function
import threading
from collections import OrderedDict
from pymesos import Scheduler
from addict import Dict
from twitter.common import log

TASK_CPU = 0.1
TASK_MEM = 32
EXECUTOR_CPUS = 0.1
EXECUTOR_MEM = 32

class GodScheduler(Scheduler):

    def __init__(self,
            state,
            state_provider,
            framework_info,
            executor_cmd,
            kazoo,
            scheduler_key):
        """
        :param state:
        :param state_provider:
        :param framework_info:
        :param executor_cmd:
        :param kazoo:
        :param scheduler_key:
        """
        self._lock = threading.Lock()
        self._state = state
        self._state_provider = state_provider
        self._framework_info =framework_info
        self._executor_cmd = executor_cmd
        self._kazoo = kazoo
        self._scheduler_key = scheduler_key
        self._driver = None
        self._tasks = {}
        self._launchers = OrderedDict()
        self.stopped = threading.Event()  # An event set when the scheduler is stopped.
        self.connected = threading.Event()

    def registered(self, driver, frameworkId, masterInfo):
        with self._lock:
            log.info("Hyaline framework registered with %s in %s" %(str(frameworkId.value),str(masterInfo.pid)))
            self._driver = driver
            self._state.framework_id = frameworkId.value
            self.release = self._state.release
            self._state_provider.dump_scheduler_state(self._state)
        self.connected.set()

    def resourceOffers(self, driver, offers):
        filters = {'refuse_seconds': 5}

        for offer in offers:
            print("=============================")
            print(offer)
            cpus = self.getResource(offer.resources, 'cpus')
            mem = self.getResource(offer.resources, 'mem')
            if cpus < TASK_CPU or mem < TASK_MEM:
                continue

            # task = Dict()
            # task_id = str(uuid.uuid4())
            # task.task_id.value = task_id
            # task.agent_id.value = offer.agent_id.value
            # task.name = 'task {}'.format(task_id)
            # task.executor = self.executor
            # task.data = encode_data('Hello from task {}!'.format(task_id))
            #
            # task.resources = [
            #     dict(name='cpus', type='SCALAR', scalar={'value': TASK_CPU}),
            #     dict(name='mem', type='SCALAR', scalar={'value': TASK_MEM}),
            # ]

            # driver.launchTasks(offer.id, [task], filters)

    def getResource(self, res, name):
        for r in res:
            if r.name == name:
                return r.scalar.value
        return 0.0

    def statusUpdate(self, driver, update):
        log.debug('Status update TID %s %s',
                      update.task_id.value,
                      update.state)

