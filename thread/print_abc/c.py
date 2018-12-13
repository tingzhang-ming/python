import threading
import random
import time

global a, b, c
a = threading.Semaphore(1)
b = threading.Semaphore(0)
c = threading.Semaphore(0)


def print_str(s):
    print s
    a = random.randint(1, 100)/100.0
    time.sleep(a)


class ThreadA(threading.Thread):

    def run(self):
        global a, b, c
        for i in range(10):
            a.acquire()
            print_str("A")
            b.release()


class ThreadB(threading.Thread):

    def run(self):
        global a, b, c
        for i in range(10):
            b.acquire()
            print_str("B")
            c.release()


class ThreadC(threading.Thread):

    def run(self):
        global a, b, c
        for i in range(10):
            c.acquire()
            print_str("C")
            a.release()


if __name__ == '__main__':
    ThreadA().start()
    ThreadB().start()
    ThreadC().start()
