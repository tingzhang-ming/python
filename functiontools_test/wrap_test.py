from functools import wraps


def a():
    """a docstring"""
    print "i am a"


@wraps(a)
def b():
    """b docstring"""
    print "i am b"


def t1():
    print a.__doc__
    print b.__doc__
    a()
    b()
    print a.__name__
    print b.__name__
    """
a docstring
a docstring
i am a
i am b
a
a
    """

if __name__ == '__main__':
    t1()
