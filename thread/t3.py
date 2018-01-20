from threading import BoundedSemaphore


def t1():
    a = BoundedSemaphore(3)
    print a.release()
    print a.acquire()
    print a.acquire()
    print a.acquire()
    print a.release()
    print a.acquire(False)


if __name__ == '__main__':
    t1()
