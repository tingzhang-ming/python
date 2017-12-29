
def t1():
    print __file__
# /root/github/python/dunder/some.py


class A(object):

    def __init__(self):
        self.a = 'hello'

    def put(self, a):
        print a


class B(A):

    def put(self, a):
        self.a = a
        print "done"


def t2():
    a = A()
    print a.__class__
    # < class '__main__.A'>


def t3():
    a = B()
    a.put('aaa')
    a.__class__ = A
    a.put('aaa')
# done
# aaa


if __name__ == '__main__':
    t3()
