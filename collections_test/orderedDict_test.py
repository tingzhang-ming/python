from collections import OrderedDict


def t1():
    d = OrderedDict(
        a='a',
        b='b',
        c='c'
    )
    for k, v in d.items():
        print( k, ': ', v)
# a :  a
# c :  c
# b :  b


def t2():
    d1 = dict(
        a='a',
        b='b',
        c='c'
    )
    d2 = dict(
        a='a',
        b='b',
        c='c'
    )
    print(d1 == d2)
    d3 = OrderedDict(
        a='a',
        b='b',
        c='c'
    )
    d4 = OrderedDict(
        a='a',
        b='b',
        c='c'
    )
    print(d3 == d4)

    d5 = OrderedDict()
    d5['a'] = 'a'
    d5['b'] = 'b'

    d6 = OrderedDict()
    d6['a'] = 'a'
    d6['b'] = 'b'
    print(d5 == d6)
    # True
    # True
    # True


def t3():
    d = dict(
        a=2,
        b=1,
        c=8
    )
    kd = OrderedDict(d)
    print(kd)
    kd2 = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    print(kd2)
    kd3 = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print(kd3)
    # OrderedDict([('a', 2), ('c', 8), ('b', 1)])
    # OrderedDict([('a', 2), ('b', 1), ('c', 8)])
    # OrderedDict([('b', 1), ('a', 2), ('c', 8)])


if __name__ == '__main__':
    t3()
