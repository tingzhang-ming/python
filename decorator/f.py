from functools import wraps


def decorator(decorated):
    @wraps(decorated)
    def inner(*args, **kwargs):
        out = apply(decorated)
        if isinstance(out, tuple) > 0:
            print 'da yu 0'
        else:
            print out
        return out
    return inner


@decorator
def t1():
    return 'a'


@decorator
def t2():
    return 'a', 'b'


if __name__ == '__main__':
    t1()
    t2()
