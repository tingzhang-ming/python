from abc import ABCMeta, abstractmethod


class AbstractGamePlayer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, user, password): pass

    @abstractmethod
    def kill_boss(self): pass

    @abstractmethod
    def upgrade(self): pass
    
    @abstractmethod
    def get_proxy(self): pass
