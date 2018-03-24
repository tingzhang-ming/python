# encoding: utf-8
import time


class Timeit(object):

    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self._wrapped(*args, **kwargs)
        print "elapsed time is %s" %(time.time() - start_time)
        return result


@Timeit
def test():
    time.sleep(1)
    return "test"
# elapsed time is 1.00059103966


class A(object):

    @Timeit
    def test(self):
        time.sleep(1)
        return "test"
# Traceback (most recent call last):
#   File "/root/github/python/decorator/i.py", line 51, in <module>
#     a.test()
#   File "/root/github/python/decorator/i.py", line 11, in __call__
#     result = self._wrapped(*args, **kwargs)
# TypeError: test() takes exactly 1 argument (0 given)


class Timeit2(object):

    def __init__(self, func):
        self._wrapped = func

    def __call__(self, *args, **kwargs):
        print "__call__"
        start_time = time.time()
        result = self._wrapped(*args, **kwargs)
        print "elapsed time is %s" %(time.time() - start_time)
        return result

    # def __get__(self, instance, owner):
    #     print "__get__"
    #     print instance
    #     print owner
    #     return lambda *args, **kwargs: self._wrapped(instance, *args, **kwargs)
    def __get__(self, instance, owner):
        print "__get__"
        print instance
        print owner

        def call(*args, **kwargs):
            start_time = time.time()
            result = self._wrapped(instance, *args, **kwargs)
            print "elapsed time is %s" % (time.time() - start_time)
            return result
        return call


class A2(object):

    @Timeit2
    def test(self):
        time.sleep(1)
        print 'test done'
        return "test"
# __get__
# <__main__.A2 object at 0x7f5e2e52fed0>
# <class '__main__.A2'>
# test done
# elapsed time is 1.00088715553

# test 方法变成了修饰符，当调用test方法时，调用__get__的返回值


@Timeit2
def test2():
    time.sleep(1)
    return "test"

# __call__
# elapsed time is 1.00077986717

if __name__ == '__main__':
    test2()
