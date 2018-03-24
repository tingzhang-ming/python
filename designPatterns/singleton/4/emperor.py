# encoding: utf-8


# 这样的单例模式，每次的__init__会生效
class Emperor2(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        print cls._instance is None
        if cls._instance:
            return cls._instance
        cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.name = None

    def say(self):
        print "my name: %s" % self.name


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super(Singleton, cls).__init__(*args, **kwargs)
        __new__o = cls.__new__

        @staticmethod
        def __new__(cls, *args, **kwargs):
            if cls._instance:
                return cls._instance
            cls._instance = __new__o(cls, *args, **kwargs)
            return cls._instance
        cls.__new__ = __new__


class Emperor(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.name = None

    def say(self):
        print "my name: %s" % self.name