

def hello(fn):
    def wrapper(*args, **kwds):
        print args
        print kwds
        len_args = len(args)
        if len_args > 0:
            print isinstance(args[0], Test)
            print args[0].__class__.__name__

        print "hello", fn.__name__
        fn(*args, **kwds)
        print "bye", fn.__name__
        print "======================="
    return wrapper


class Test(object):

    def __init__(self):
        self.a = 'hahah'

    @hello
    def test(self):
        print self.a


def t1():
    t = Test()
    t.test()


if __name__ == '__main__':
    t1()
