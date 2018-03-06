
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("calling Meta's __new__", cls)
        return super(Meta, cls).__new__(cls, name, bases, dct)

    def __init__(cls, *args, **kwargs):
        print "Meta __init__"
        super(Meta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("calling Meta's __call__", cls)
        # i = cls.__new__(cls)
        # i.__init__(*args, **kwargs)
        # return i
        return ""


class A(object):
    __metaclass__ = Meta

    def __new__(cls, *args, **kwargs):
        print("calling A's __new__")
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        print("calling A's __init__")


if __name__ == '__main__':
    a = A()


# ("calling Meta's __new__", <class '__main__.Meta'>)
# ("calling Meta's __call__", <class '__main__.A'>)
# calling A's __new__
# calling A's __init__
