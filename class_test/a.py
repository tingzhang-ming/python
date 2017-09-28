
class Test(object):

    N = 100

    def __init__(self, name):
        self.name = name

    @staticmethod
    def add(a):
        print "add", a

    @classmethod
    def my(cls):
        print cls.N

if __name__ == '__main__':
    Test.add("hahhaha")
    t = Test("mhc")
    t.add("asdasd")

    t.my()

