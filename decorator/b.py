
def dec(a=None, *args, **kwds):
    def hello(fn):
        def wrapper(*args, **kwds):
            print "hello", fn.__name__
            print "i get %s" % str(a)
            fn(*args, **kwds)
            print "bye", fn.__name__
            print "======================="

        return wrapper
    return hello

@dec()
def test1():
    print "i am test1"

@dec("hahahah")
def test2():
    print "i am test2"


if __name__ == '__main__':
    test1()
    test2()

# hello test1
# i get None
# i am test1
# bye test1
# =======================
# hello test2
# i get hahahah
# i am test2
# bye test2
# =======================

