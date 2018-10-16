from abc import ABCMeta, abstractmethod
from threading import RLock
import copy


class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, observable, context):
        pass


class Observable(object):

    def __init__(self):
        self._changed = False
        self._obs = []
        self._lock = RLock()

    def notify_observers(self, arg=None):
        with self._lock:
            if not self._changed:
                return
            obs_copy = copy.deepcopy(self._obs)
            self.clear_changed()
        for ob in obs_copy:
            ob.update(self, arg)

    def add_observer(self, observer):
        with self._lock:
            if observer is None:
                raise ValueError("observer can't be none")
            if observer not in self._obs:
                self._obs.append(observer)

    def delete_observer(self, observer):
        with self._lock:
            try:
                self._obs.remove(observer)
            except ValueError:
                pass

    def clear_changed(self):
        with self._lock:
            self._changed = False

    def has_changed(self):
        with self._lock:
            return self._changed

    def count_observers(self):
        with self._lock:
            return len(self._obs)

    def set_changed(self):
        with self._lock:
            self._changed = True




