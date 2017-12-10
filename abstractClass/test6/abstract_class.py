from abc import ABCMeta,abstractmethod

class Abstract_test(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method1(self, name):
        pass

    @abstractmethod
    def method2(self, name):
        self.method1(name)



