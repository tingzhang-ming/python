# encoding: utf-8
import random


def t1():
    print random.random()
    # 0.428055345717


def t2():
    print random.randint(1, 100)
    # 64  包含100


def t3():
    # 输出 100 <= number < 1000 间的偶数
    print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

    # 输出 100 <= number < 1000 间的其他数
    print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)
    # randrange(100, 1000, 2):  986
    # randrange(100, 1000, 3):  715


def t4():
    a = ["haha", "lala", "daada"]
    print random.choice(a)
    # haha


if __name__ == '__main__':
    t4()
