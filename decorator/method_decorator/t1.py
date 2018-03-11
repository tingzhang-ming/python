
def d(fun):
    print fun.__name__
    return fun


def d2(fun):
    def inner(cls, *args, **kwargs):
        print cls.__class__.__name__
        return fun(cls, *args, **kwargs)
    return inner


class A(object):

    @d2
    def a(self):
        print "111111111111"


if __name__ == '__main__':
    a = A()
    a.a()
