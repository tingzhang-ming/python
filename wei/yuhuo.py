# encoding: utf-8


def t1():
    print 3 ^ 5
    print 6 ^ 5
    # 6
    # 3
    # 011 ^ 101 = 110
    # 110 ^ 101 = 011


def t2():
    """ swap """
    a = 100
    b = 222
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print a, b
    # 222 100


if __name__ == '__main__':
    t2()
