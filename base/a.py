from collections import OrderedDict


def a():
    return ["h","a","lala","b"]


def b():
    out = a()

    return out + ["a1"]


def t1():
    p1, p2, p3, p4, p5 = b()
    print p1
    print p2
    print p3
    print p4
    print p5


if __name__ == '__main__':
    t1()
