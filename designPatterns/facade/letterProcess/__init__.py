from abc import ABCMeta, abstractmethod


class AbstractLetterProcess(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, context):
        pass

    @abstractmethod
    def fill(self, address):
        pass

    @abstractmethod
    def send(self):
        pass
