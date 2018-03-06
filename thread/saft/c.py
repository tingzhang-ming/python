import time
from threading import Thread

l = [0, 1, 2, 3]


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        l[0] += 1
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Test(object):
    __metaclass__ = Singleton
    a = "2"


def ap():
    for _ in range(10):
        time.sleep(0.1)
        a = Test()
        print a


if __name__ == '__main__':
    for i in range(5):
        Thread(target=ap).start()
    time.sleep(15)
    print l

# [496, 1, 2, 3]
