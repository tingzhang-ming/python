

class A1(object):

    @property
    def a(self):
        return "sfafadf"


def t1():
    a = A1()
    print a.a
    a.a = "haha"
    print a.a


if __name__ == '__main__':
    t1()
