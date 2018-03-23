""" unhashable """


class Descriptor(object):

    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        print '__get__', instance, owner
        return instance.__dict__.get(self.label)

    def __set__(self, instance, value):
        print '__set__'
        instance.__dict__[self.label] = value


class Foo(list):
    x = Descriptor('x')
    y = Descriptor('y')

f = Foo()
f.x = 5
print f.x
f.y = 4
print f.x

# __set__
# __get__ [] <class '__main__.Foo'>
# 5
# __set__
# __get__ [] <class '__main__.Foo'>
# 5