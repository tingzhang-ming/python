from abc import ABCMeta, abstractmethod
from observer import Observable


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
        super(HanFeiZi, self).__init__()

    def have_breakfast(self):
        print "i have_breakfast"
        self.set_changed()
        self.notify_observers("han fei zi have_breakfast")

    def have_fun(self):
        print "i have fun"
        self.set_changed()
        self.notify_observers("han fei zi have fun")

