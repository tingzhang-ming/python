from abc import ABCMeta, abstractmethod

class Abstract_test(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get(self):
        print(self.name)

    @abstractmethod
    def set(self, name):
        print("i am abstractmethod")
