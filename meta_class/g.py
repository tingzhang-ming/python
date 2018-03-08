
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("calling Meta's __new__", cls)
        return super(Meta, cls).__new__(cls, name, bases, dct)

    def __init__(self, *args, **kwargs):
        print "Meta __init__"
        super(Meta, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("calling Meta's __call__", self)
        return super(Meta, self).__call__(*args, **kwargs)

    def a(cls):
        print "aaaa"


class A(object):
    __metaclass__ = Meta

    def __new__(cls, *args, **kwargs):
        print("calling A's __new__")
        return super(A, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        print("calling A's __init__")



if __name__ == '__main__':
    A.a()
    a = A()


# ("calling Meta's __new__", <class '__main__.Meta'>)
# ("calling Meta's __call__", <class '__main__.A'>)
# calling A's __new__
# calling A's __init__
