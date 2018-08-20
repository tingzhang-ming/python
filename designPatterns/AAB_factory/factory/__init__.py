from abc import ABCMeta, abstractmethod


class AbstractHumanFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_human(self, name):
        pass