from abc import ABCMeta, abstractmethod


class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, context):
        pass


class Lisi(Observer):

    def update(self, context):
        print "li si observe han fei zi"
        print "bao gao: ", context


class Wangsi(Observer):

    def update(self, context):
        print "Wang si observe han fei zi"
        print "Wo kan jian: ", context
