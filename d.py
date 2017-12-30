from __future__ import print_function
import sys


def t1():
    print("haha", file=sys.stderr)


def t2():
    with open('/tmp/a.txt', 'w') as o1:
        print("haha", file=o1)
    with open('/tmp/a.txt', 'rb') as o2:
        print(o2.read())


def test(a=1, b=2):
    print(a)


def t3():
    test(**dict(a=111))


def t4():
    chunk_sum = 55
    size = 100
    print(chunk_sum * 100 / size)

if __name__ == '__main__':
    t4()

