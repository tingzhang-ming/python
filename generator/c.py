
class Fab(object):

    def __init__(self, max_n):
        self.max = max_n
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration


def t1():
    for n in Fab(5):
        print n


def t2():
    f = Fab(5)
    it = iter(f)
    while True:
        try:
            print next(it)
        except StopIteration:
            print "end"
            break


if __name__ == '__main__':
    t2()
