from abc import ABCMeta, abstractmethod


class AbstractStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def operate(self):
        pass


class BackDoor(AbstractStrategy):

    def operate(self):
        print("back door...")


class GivenGreenLight(AbstractStrategy):
    def operate(self):
        print("given green light...")


class BlockEnemy(AbstractStrategy):
    def operate(self):
        print("block enemy...")


