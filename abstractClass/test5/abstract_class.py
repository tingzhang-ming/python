from abc import ABCMeta,abstractmethod


class AbstractTest(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method1(self, name):
        pass



