# encoding: utf-8
from collections import deque


def t1():
    d = deque([1, 2, 3, 4])
    print d
    d.extendleft([99, 100])
    print d
    print d.popleft()
    print d
    # deque([1, 2, 3, 4])
    # deque([100, 99, 1, 2, 3, 4])
    # 100
    # deque([99, 1, 2, 3, 4])


def t2():
    d = deque([1, 2, 3, 4])
    print d
    # d.rotate(1)    # 将右端的一个元素移到左端
    # print d
    # deque([1, 2, 3, 4])
    # deque([4, 1, 2, 3])
    # d.rotate(-2)
    # print d
    # deque([1, 2, 3, 4])
    # deque([3, 4, 1, 2])
    d.rotate(-1)
    print d
    # deque([1, 2, 3, 4])
    # deque([2, 3, 4, 1])

if __name__ == '__main__':
    t2()
