from abc import ABCMeta, abstractmethod


class AbstractWomen(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_request(self):
        pass
