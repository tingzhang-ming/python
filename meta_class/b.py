

class FooOrBar(type):

    def __new__(cls, name, bases, attrs):
        if 'foo' in attrs and 'bar' in attrs:
            raise TypeError('Class %s cannot contain both `foo` and `bar` attributes.' % name)
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError('Class %s must provide either a `foo` attribute or a `bar` attribute.' % name)
        return super(FooOrBar, cls).__new__(cls, name, bases, attrs)


class Valid(object):

    __metaclass__ = FooOrBar

    foo = 42


# class Valid2(object):
#
#     __metaclass__ = FooOrBar


# -------------------------------------------------------


class FooOrBar2(type):

    def __new__(cls, *args, **kwargs):
        answer = super(FooOrBar2, cls).__new__(cls, *args, **kwargs)
        print args
        print kwargs
        if hasattr(answer, 'foo') and hasattr(answer, 'bar'):
            raise TypeError('Class %s cannot contain both `foo` and `bar` attributes.' % name)
        if not hasattr(answer, 'foo') and not hasattr(answer, 'bar'):
            raise TypeError('Class %s must provide either a `foo` attribute or a `bar` attribute.' % name)
        return answer


class Valid3(object):

    __metaclass__ = FooOrBar2

    foo = 42


if __name__ == '__main__':
    v = Valid3()
