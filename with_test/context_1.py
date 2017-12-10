from contextlib import closing


class A(object):

    def open(self):
        print 'open'
        return self

    def close(self):
        print 'close'


def t1():
    a = A()
    with closing(a.open()) as f:
        print 'haha'
# open
# haha
# close


def t2():
    a = A()
    with closing(a) as f:
        print 'haha'

# haha
# close


def t3():
    a = A()
    with closing(a):
        print 'haha'
#
# haha
# close


if __name__ == '__main__':
    t3()
