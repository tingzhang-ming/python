# encoding: utf-8


def t1():
    print 3 | 5
    # 7
    # 011 | 101 = 111


def t2():
    target = 103
    print target | 1  # 大于等于target的最小奇数
    print (target | 1) - 1  # 小于等于target的最大偶数


if __name__ == '__main__':
    t2()
