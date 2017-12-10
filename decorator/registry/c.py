import sys
from functools import wraps
from collections import OrderedDict
registry = OrderedDict()


def register(decorated):
    registry[decorated.__name__] = decorated
    return decorated


def debug(fn=None, log_output=False):
    """
    Function/method decorator to trace calls via debug logging. Acts as
    pass-thru if not at LOG_LEVEL=DEBUG. Normally this would kill perf but
    this application doesn't have significant throughput.
    """
    def _decorate(fn, *args, **kwargs):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                # because we have concurrent processes running we want
                # to tag each stack with an identifier for that process
                msg = "[{}]".format(sys.argv[1])
            except IndexError:
                msg = "[pre_start]"
            len_args = len(args)
            if len_args > 0:
                cls_name = args[0].__class__.__name__.lower()
                name = '{}.{}'.format(cls_name, fn.__name__)
            else:
                name = fn.__name__
            print('%s %s start' % (msg, name))
            out = apply(fn, args, kwargs)
            if log_output:  # useful for checking status flags
                print('%s %s end: %s' % (msg, name, out))
            else:
                print('%s %s end' % (msg, name))
            return out
        return wrapper
    if fn:
        return _decorate(fn)
    return _decorate


@register
@debug
def foo():
    print 'foo'
    return 3


@register
@debug
def bar():
    return 5


def t1():
    print registry
    registry['foo']()

if __name__ == '__main__':
    t1()
