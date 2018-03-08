import abc
from functools import wraps


class AbstractDict(object):

    __metaclass__ = abc.ABCMeta

    def foo(self):
        return None


class MyDict(object):
    pass


class MyDict2(AbstractDict):
    pass


def t1():
    AbstractDict.register(dict)
    AbstractDict.register(MyDict)
    print issubclass(dict, AbstractDict)
    print isinstance({}, AbstractDict)
    print issubclass(MyDict, AbstractDict)
    print issubclass(MyDict2, AbstractDict)
    # True
    # True
    # True
    # True
# --------------------------------------------------


class AbstractDict2(object):

    __metaclass__ = abc.ABCMeta

    def foo(self):
        return None

    @classmethod
    def myregister(cls, subcls):
        cls.register(subcls)
        return subcls


@AbstractDict2.myregister
class MyDict21(object):
    pass


class MyDict22(AbstractDict2):
    pass


def t2():
    AbstractDict2.register(dict)
    print issubclass(dict, AbstractDict2)
    print isinstance({}, AbstractDict2)
    print issubclass(MyDict21, AbstractDict2)
    print issubclass(MyDict22, AbstractDict2)
    # True
    # True
    # True
    # True
# ----------------------------------------------------


class MyABCMeta(abc.ABCMeta):

    def myregister(cls, subcls):
        cls.register(subcls)
        return subcls


class AbstractDict3(object):

    __metaclass__ = MyABCMeta

    def foo(self):
        return None


@AbstractDict3.myregister
class MyDict31(object):
    pass


class MyDict32(AbstractDict3):
    pass


def t3():
    AbstractDict3.register(dict)
    print issubclass(dict, AbstractDict3)
    print isinstance({}, AbstractDict3)
    print issubclass(MyDict31, AbstractDict3)
    print issubclass(MyDict32, AbstractDict3)
    a = MyDict31()
    print isinstance(a, AbstractDict3)
    # True
    # True
    # True
    # True
    # True

if __name__ == '__main__':
    t3()
