from functools import wraps


def debug(fn=None, log_output=False):
    def _decorate(fn, *args, **kwargs):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            len_args = len(args)
            if len_args > 0:
                cls_name = args[0].__class__.__name__.lower()
                name = '{}.{}'.format(cls_name, fn.__name__)
            else:
                name = fn.__name__
            print('%s start' % name)
            out = apply(fn, args, kwargs)
            if log_output:  # useful for checking status flags
                print('%s end: %s' % (name, out))
            else:
                print('%s end' % name)
            return out
        return wrapper
    if fn:
        print "if fn"
        return _decorate(fn)
    return _decorate


# @debug
# def a():
#     print 'i am a'
# if fn
# a start
# i am a
# a end


# @debug
# def b(x, y):
#     return x + y
# if fn
# int.b start
# int.b end


@debug(log_output=True)
def c(x, y):
    return x + y
# int.c start
# int.c end: 3


if __name__ == '__main__':
    c(1, 2)
