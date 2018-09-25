from abc import ABCMeta, abstractmethod


class AbstractUserInfo(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_number(self):
        pass


class UserInfo(AbstractUserInfo):

    def get_name(self):
        print "name is"
        return ""

    def get_number(self):
        print "number is"
        return 0

