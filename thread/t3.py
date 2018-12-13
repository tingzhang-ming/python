from threading import BoundedSemaphore, Semaphore


def t1():
    a = BoundedSemaphore(3)
    # print a.release()
    print a.acquire()
    print a.acquire()
    print a.acquire()
    print a.release()
    print a.acquire(False)


def t2():
    a = Semaphore(0)
    print a.release()
    print a.acquire()
    print a.release()
# None
# True
# None


if __name__ == '__main__':
    t2()
