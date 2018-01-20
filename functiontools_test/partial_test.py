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

if __name__ == '__main__':
    t2()
