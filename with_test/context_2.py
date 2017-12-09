import threading
from contextlib import contextmanager
from collections import namedtuple

lock = threading.Lock()


def safeWriteToFile(openedFile, content):
    lock.acquire()
    openedFile.write(content)
    lock.release()


@contextmanager
def loudLock():
    print 'Locking'
    lock.acquire()
    yield
    print 'Releasing'
    lock.release()


def t1():
    with loudLock():
        print 'Lock is locked: %s' % lock.locked()
        print 'Doing something that needs locking'

    # Output:
    # Locking
    # Lock is locked: True
    # Doing something that needs locking
    # Releasing


@contextmanager
def test():
    print 'enter'
    yield namedtuple('t', ['a'])(a='haha')
    print 'exit'


def t2():
    with test() as f:
        print f.a
#

if __name__ == '__main__':
    t2()
