from abc import ABCMeta, abstractmethod

class Abstract_test1(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name1 = name
        self.name2 = "hahah"

    @abstractmethod
    def get1(self):
        print(self.name1)

    @abstractmethod
    def set1(self, name):
        print("i am abstractmethod")
