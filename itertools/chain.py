from itertools import chain


def t1():
    a = {"a": 1, "aa": 2}
    b = {"b": 11, "bb": 22}
    print chain(a.items(), b.items())
    print dict(chain(a.items(), b.items()))
# <itertools.chain object at 0x0000000004F38BE0>
# {'a': 1, 'aa': 2, 'b': 11, 'bb': 22}


def t2():
    a = {"a": 1, "aa": 2}
    b = {"b": 11, "bb": 22}
    for k, v in chain(a.items(), b.items()):
        print "k: {}, v: {}".format(k, v)
# k: a, v: 1
# k: aa, v: 2
# k: b, v: 11
# k: bb, v: 22


def t3():
    a = ["1", "2", "3"]
    b = ["a", "b"]
    print list(chain(a, b))
    for i in chain(a, b):
        print i
# ['1', '2', '3', 'a', 'b']
# 1
# 2
# 3
# a
# b

if __name__ == '__main__':
    t3()
