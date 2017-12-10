

class BubbleExceptions(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Bubbling up exception: %s.' % exc_val)
            return False


def t1():
    with BubbleExceptions():
        print 5 + 5
# 10


def t2():
    with BubbleExceptions():
        print 5 / 0
# Bubbling up exception: integer division or modulo by zero.
# Traceback (most recent call last):
#   File "/root/github/python/with_test/a.py", line 25, in <module>
#     t2()
#   File "/root/github/python/with_test/a.py", line 22, in t2
#     print 5 / 0
# ZeroDivisionError: integer division or modulo by zero


class BubbleExceptions2(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Bubbling up exception: %s.' % exc_val)
            return True


def t3():
    with BubbleExceptions2():
        print 5 / 0
# Bubbling up exception: integer division or modulo by zero.


class BubbleExceptions3(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print exc_type
            print exc_val
            print exc_tb
            return True
# <type 'exceptions.ZeroDivisionError'>
# integer division or modulo by zero
# <traceback object at 0x7efff7a68290>


def t4():
    with BubbleExceptions3():
        print 5 / 0


if __name__ == '__main__':
    t4()
