
def t1():
    f = lambda x, y, z: x+y+x
    print f(1, 2, 3)
    # 4


def t2():
    f = lambda: True
    print f()


def t3():
    foo = [2, 8, 9, 22]
    print filter(lambda x: x % 3 == 0, foo)
    print map(lambda x: x * 2 + 1, foo)
    print reduce(lambda x, y: x + y, foo)
    print reduce(lambda x, y: x +y, foo, 100)
    # [9]
    # [5, 17, 19, 45]
    # 41
    # 141


def t4():
    print map(lambda x, y: max([x, y]), [1, 2, 3], [2, 5, 0])
    # [2, 5, 3]


def t5():
    def test(a):
        # print a
        return a
    t = lambda: test('hello')
    print t()

if __name__ == '__main__':
    t5()
