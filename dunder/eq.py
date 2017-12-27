

class MyClass(object):

    def __eq__(self, other):
        return type(self) == type(other)


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print a == b
# True
"""
__ne__  !=
__lt__  <
__le__  <=
__gt__  >
__ge__  >=
"""
