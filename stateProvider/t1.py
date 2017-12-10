from localState import LocalState


class T1(object):

    def __init__(self):
        self._a = "haah"

    def set(self, value):
        self._a = value

    def get(self):
        return self._a

key = "test"


def test1():
    t = T1()
    t.set("2222")
    print t.get()
    ls = LocalState()
    ls.put(key, t)
    t2 = ls.get(key)
    print t2.get()


def test2():
    ls = LocalState()
    t2 = ls.get(key)
    print t2.get()
    t2.set("333")
    print t2.get()


if __name__ == '__main__':
    test2()
