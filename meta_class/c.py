

class Logged(type):
    """
    A metaclass that causes classes that it creates to log their function calls.
    """

    def __new__(cls, name, bases, attrs):
        for k, v in attrs.items():
            if callable(v):
                attrs[k] = cls.log_call(v)
        return super(Logged, cls).__new__(cls, name, bases, attrs)

    @staticmethod
    def log_call(fxn):
        """
        Given a function, wrap it with some logging code and return the wrapped function. 
        """
        def inner(*args, **kwargs):
            print 'The function %s was called with arguments %r and ' \
                  'keyword arguments %r.' % (fxn.__name__, args, kwargs)
            try:
                response = fxn(*args, **kwargs)
                print 'The function call to %s was successful.' % fxn.__name__
                return response
            except Exception as exc:
                print 'The function call to %s raised an execption: %r' % (fxn.__name__, exc)
                raise
        return inner


class MyClass(object):

    __metaclass__ = Logged

    def foo(self):
        pass

    def bar(self):
        raise TypeError('oh nose!')


if __name__ == '__main__':
    obj = MyClass()
    obj.foo()
    obj.bar()

# /usr/bin/python2.7 /root/github/python/meta_class/c.py
# The function foo was called with arguments (<__main__.MyClass object at 0x7f245351b850>,) and keyword arguments {}.
# The function call to foo was successful.
# The function bar was called with arguments (<__main__.MyClass object at 0x7f245351b850>,) and keyword arguments {}.
# The function call to bar raised an execption: TypeError('oh nose!',)
# Traceback (most recent call last):
#   File "/root/github/python/meta_class/c.py", line 46, in <module>
#     obj.bar()
#   File "/root/github/python/meta_class/c.py", line 23, in inner
#     response = fxn(*args, **kwargs)
#   File "/root/github/python/meta_class/c.py", line 40, in bar
#     raise TypeError('oh nose!')
# TypeError: oh nose!
