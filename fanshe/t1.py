import inspect


def convert_fn_args(fn):
    """
    :type fn:
    :rtype: (list[str], dict[str, any])
    """
    arg_specs = inspect.getargspec(fn)
    args = arg_specs.args
    defaults = arg_specs.defaults
    if defaults is None:
        defaults = []
    pos = len(args) - len(defaults)
    return args[:pos], dict((args[pos + i], defaults[i]) for i in range(len(defaults)))


def test1(a, b=1):
    print a
    print b


def t1():
    print convert_fn_args(test1)
# (['a'], {'b': 1})

if __name__ == '__main__':
    t1()

