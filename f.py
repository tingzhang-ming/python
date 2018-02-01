

a = {'a': 1}


def t1():
    try:
        b = a['b']
    except IndexError:
        print 'key error'
        return
    finally:
        a.clear()


def t2():
    for i in range(5, 0, -1):
        print i


def t3():
    print 235345 & 0x7fffffff


def t4():
    a = 1
    b = 22222
    b = a^b
    a = a^b
    b = a^b
    print a
    print b


if __name__ == '__main__':
    t4()
