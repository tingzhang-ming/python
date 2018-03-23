
class Descriptor(object):
    def __init__(self):
        # notice we aren't setting the label here
        self.label = None

    def __get__(self, instance, owner):
        print '__get__. Label = %s' % self.label
        return instance.__dict__.get(self.label, None)

    def __set__(self, instance, value):
        print '__set__'
        instance.__dict__[self.label] = value


class DescriptorOwner(type):
    def __new__(cls, name, bases, attrs):
        # find all descriptors, auto-set their labels
        for n, v in attrs.items():
            if isinstance(v, Descriptor):
                v.label = n
        return super(DescriptorOwner, cls).__new__(cls, name, bases, attrs)


class Foo(object):
    __metaclass__ = DescriptorOwner
    x = Descriptor()


f = Foo()
f.x = 5
print f.x

# __set__
# __get__. Label = x
# 5
