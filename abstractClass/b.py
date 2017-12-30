import abc


class AbstractDict(object):

    __metaclass__ = abc.ABCMeta

    def foo(self):
        return None


class MyDict(object):
    pass


class MyDict2(AbstractDict):
    pass

if __name__ == '__main__':
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
