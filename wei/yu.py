# encoding: utf-8


def t1():
    print(3 & 5)
    # 1
    # 011 & 101 = 001


def t2():
    """ 判断奇偶"""
    target = 100
    if target & 1 == 1:
        print '奇'
    else:
        print '偶'


if __name__ == '__main__':
    t2()
