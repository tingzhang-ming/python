from abc import ABCMeta, abstractmethod


class AbstractGroup(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def change(self): pass

    @abstractmethod
    def find(self): pass

    @abstractmethod
    def plan(self): pass
