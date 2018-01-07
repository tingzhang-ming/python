

class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


def t1():
    x = Bunch(name="Jayne Cobb", position="Public Relations")
    print x.name
    """Jayne Cobb
    """


def t2():
    T = Bunch
    t = T(left=T(left="a", right="b"), right=T(left="c"))
    print t.left
    print t.left.right

if __name__ == '__main__':
    t2()
