

def t1():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print a == b
    c = [i for i in reversed(a)]
    print c
    print a


def t2():
    a = ['a', 'b']
    b = ""
    for i in a:
        b += i
    print b


def t3():
    for i in range(0, 1):
        print 1 * 10 ** i


def t4():
    print max(1, 2)

if __name__ == "__main__":
    t4()
