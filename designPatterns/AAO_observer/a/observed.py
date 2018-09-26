from abc import ABCMeta, abstractmethod


class Observable(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def delete_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, context):
        pass


class AbstractHanFeiZi(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def have_breakfast(self):
        pass

    @abstractmethod
    def have_fun(self):
        pass


class HanFeiZi(Observable, AbstractHanFeiZi):

    def __init__(self):
        self._observer_list = []

    def add_observer(self, observer):
        self._observer_list.append(observer)

    def delete_observer(self, observer):
        if observer in self._observer_list:
            self._observer_list.remove(observer)

    def notify_observers(self, context):
        for obs in self._observer_list:
            obs.update(context)

    def have_breakfast(self):
        print "i have_breakfast"
        self.notify_observers("han fei zi have_breakfast")

    def have_fun(self):
        print "i have fun"
        self.notify_observers("han fei zi have fun")

