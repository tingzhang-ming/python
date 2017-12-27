import functools

def requires_ints(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        kwargs_values = [i for i in kwargs.values()]
        for arg in list(args) + kwargs_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' %decorated.__name__)
        return decorated(*args, **kwargs)
    return inner

@requires_ints
def foo(x, y):
    return x + y

if __name__ == '__main__':
    print foo(2, 3)
    print foo(2.5, 3)