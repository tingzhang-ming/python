from abc import ABCMeta, abstractmethod


class Human(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def get_sex(self):
        pass