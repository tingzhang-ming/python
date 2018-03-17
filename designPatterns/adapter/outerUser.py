from abc import ABCMeta, abstractmethod


class AbstractOuterUser(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_user_base_info(self):
        pass

    @abstractmethod
    def get_user_home_info(self):
        pass


class OuterUser(AbstractOuterUser):

    def get_user_base_info(self):
        return {"name": "mmm", "sex": "nan"}

    def get_user_home_info(self):
        return {"number": "123", "address": "china"}

