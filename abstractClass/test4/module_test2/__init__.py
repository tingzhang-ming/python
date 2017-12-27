from abc import ABCMeta, abstractmethod

class Abstract_test2(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name2 = name

    @abstractmethod
    def get2(self):
        print(self.name2)

    @abstractmethod
    def set2(self, name):
        print("i am abstractmethod")
