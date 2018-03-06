import time
from threading import Thread

l = [0, 1, 2, 3]


class Test(object):

    def __new__(cls, *args, **kwargs):
        l[0] += 1
        return super(Test, cls).__new__(cls)


def ap():
    for _ in range(100):
        time.sleep(0.1)
        a = Test()


if __name__ == '__main__':
    for i in range(5):
        Thread(target=ap).start()
    time.sleep(15)
    print l

# [496, 1, 2, 3]
