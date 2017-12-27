

def hello(fn):
    def wrapper(*args, **kwds):
        print args
        print kwds
        print "hello", fn.__name__
        fn(*args, **kwds)
        print "bye", fn.__name__
        print "======================="
    return wrapper

@hello
def test1():
    print "i am test1"

@hello
def test2(name):
    print "test2 para is", name

@hello
@hello
def test3():
    print "i am test3"

if __name__ == '__main__':
    test1()
    test2("mhc")
    test3()

    # ()
    # {}
    # hello
    # test1
    # i
    # am
    # test1
    # bye
    # test1
    # == == == == == == == == == == == =
    # ('mhc',)
    # {}
    # hello
    # test2
    # test2
    # para is mhc
    # bye
    # test2
    # == == == == == == == == == == == =
    # ()
    # {}
    # hello
    # wrapper
    # ()
    # {}
    # hello
    # test3
    # i
    # am
    # test3
    # bye
    # test3
    # == == == == == == == == == == == =
    # bye
    # wrapper
    # == == == == == == == == == == == =