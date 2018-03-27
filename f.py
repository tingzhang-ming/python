

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


def get_value(s):
    tmp = dict(
        a='1',
        b='2',
        c='3',
        d='4',
        e='5',
        f='6',
        g='7',
        h='8',
        i='9',
        j='10',
        k='11',
        l='12',
        m='13',
        n='14',
        o='15',
        p='16',
        q='17',
        r='18',
        s='19',
        t='20',
        u='21',
        v='22',
        w='23',
        x='24',
        y='25',
        z='26',
    )
    res = ''
    for ss in s:
        try:
            int(ss)
        except ValueError:
            res += tmp[ss]
        else:
            res += ss
    return int(res)


def t5():
    a = str("n4wlk")[:4]
    print a
    print get_value(a)


def t6():
    print 5 * 1024 * 1024
    print 200 * 1024 * 1024


import time
def t7():
    print time.time()


def t8():
    print 1522059333 - 1522058433
    a = 900 + 1522059333
    now = time.time()
    print a - time.time()
    print now >= a

if __name__ == '__main__':
    t8()
