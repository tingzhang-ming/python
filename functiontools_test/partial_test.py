from functools import partial


def add(a, b):
    return a + b


def t1():
    print add(1, 2)
    add2 = partial(add, 1)
    print add2(3)
# 3
# 4


def t2():
    add2 = partial(add, 1, 2)
    print add2()
    # 3


def fun(a, b=1):
    print a
    print b
    return a + b


def t3():
    add3 = partial(fun, b=99)
    print add3(1)
# 1
# 99
# 100


if __name__ == '__main__':
    t3()
