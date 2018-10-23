from abc import ABCMeta, abstractmethod


class Role(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def accept(self, actor):
        pass


class IdiotRole(Role):
    def accept(self, actor):
        actor.act(self)


class KungFuRole(Role):
    def accept(self, actor):
        actor.act(self)
