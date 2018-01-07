

def almost_equal(x, y, places=7):
    return round(abs(x-y), places) == 0


def t1():
    print sum(0.1 for i in range(10)) == 1.0
    print almost_equal(sum(0.1 for i in range(10)), 1.0)
    # False
    # True


def t2():
    print round(0.001, 1)
    # 0.0


from decimal import *
def t3():
    print sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")
    # True

if __name__ == '__main__':
    t3()
