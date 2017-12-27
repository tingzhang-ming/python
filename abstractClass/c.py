import abc


class AbstractDuck(object):

    __metaclass__ = abc.ABCMeta

    @classmethod
    def __subclasshook__(cls, other):
        quack = getattr(other, 'quack', None)
        return callable(quack)


class Duck(object):
    def quack(self):
        pass


class Duck2(object):
    quack = 'ha'


def t1():
    print issubclass(Duck, AbstractDuck)
    print issubclass(Duck2, AbstractDuck)
    AbstractDuck.register(Duck2)
    print issubclass(Duck2, AbstractDuck)
    # True
    # False
    # False


class AbstractDuck2(object):

    __metaclass__ = abc.ABCMeta

    @classmethod
    def __subclasshook__(cls, other):
        quack = getattr(other, 'quack', None)
        if callable(quack):
            return True
        return NotImplemented


def t2():
    print issubclass(Duck, AbstractDuck2)
    print issubclass(Duck2, AbstractDuck2)
    AbstractDuck2.register(Duck2)
    print issubclass(Duck2, AbstractDuck2)
# True
# False
# True

if __name__ == '__main__':
    t2()

