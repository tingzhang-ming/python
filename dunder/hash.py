

class Meta(type):

    def __new__(cls, name,  bases, attrs):
        cls._start_id = 0
        return super(Meta, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        instance = super(Meta, cls).__call__(*args, **kwargs)
        instance.id = cls._start_id
        cls._start_id += 1
        return instance


class A(object):

    __metaclass__ = Meta

    def __init__(self):
        print "init"

    def __hash__(self):
        return self.id
# init
# 0
# init
# 1
# init
# 2
# init
# 3
# init
# 4
# init
# 5
# init
# 6
# init
# 7
# init
# 8
# init
# 9


def t1():
    for i in range(10):
        print hash(A())
#--------------------------------------
from functools import wraps


class GenID(object):

    def __init__(self):
        self._start_id = 0

    def __call__(self, cls):
        print "call"
        @wraps(cls)
        def _gen_id(*args, **kw):
            instance = cls(*args, **kw)
            if not hasattr(instance, 'id'):
                setattr(instance, 'id', self._start_id)
            else:
                instance.id = self._start_id
            self._start_id += 1
            return instance
        return _gen_id

gen_id = GenID()


@gen_id
class A2(object):

    def __init__(self):
        print "init"

    def __hash__(self):
        return self.id


def t2():
    for i in range(10):
        print hash(A2())

if __name__ == '__main__':
    t2()
