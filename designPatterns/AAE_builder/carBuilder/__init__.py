from abc import ABCMeta, abstractmethod


class CarBuilder(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sequence(self, sequence): pass

    @abstractmethod
    def get_car_model(self): pass
