

def t1():
    print(__name__)


def t2():
    from a import ta1
    ta1()
# a


def t3():
    from base.a import ta1
    ta1()
    from base import a
    print(a.__name__)
# base.a
# base.a


if __name__ == '__main__':
    t3()
