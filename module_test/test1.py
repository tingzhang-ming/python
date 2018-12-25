

def t1():
    from a import A, AB
    aa = A()
    aa.do()
    ab = AB()
    ab.do()
# ImportError: cannot import name AB


def t2():
    from a import A
    aa = A()
    aa.do()
    from a.aa import AB
    ab = AB()
    ab.do()


def t3():
    from a.aa import A
    aa = A()
    aa.do()


if __name__ == '__main__':
    t3()
