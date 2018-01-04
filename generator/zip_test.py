

def t1():
    a = zip(['a', 'b', 'c', 'd'], ['x', 'y', 'z'])
    for i in a:
        print i
# ('a', 'x')
# ('b', 'y')
# ('c', 'z')


def t2():
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    xyz = zip(x, y, z)

    print xyz
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


def t3():
    x = [1, 2, 3]
    x = zip(x)
    print x
# [(1,), (2,), (3,)]


def t4():
    x = zip()
    print x
# []


def t5():
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    xyz = zip(x, y, z)
    u = zip(*xyz)
    print u
# [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


def t6():
    x = [1, 2, 3]
    print [x] * 3
    r = zip(*[x] * 3)
    print r
    # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    # [(1, 1, 1), (2, 2, 2), (3, 3, 3)]


def t7():
    a = {"a": 1, "b": 2}
    b = {"c": 3, "b": 2}
    print zip(a, b)
    # [('a', 'c'), ('b', 'b')]

if __name__ == '__main__':
    t7()
