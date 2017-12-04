
def t1():
    for i in xrange(10):
        print i


def fab(max_n):
    n, a, b = 0, 0, 1
    l = []
    while n < max_n:
        l.append(b)
        a, b = b, a + b
        n += 1
    return l


def t2():
    print fab(5)
    # [1, 1, 2, 3, 5]


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
        raise StopIteration()


def t3():
    for n in Fab(5):
        print n
    # 1
    # 1
    # 2
    # 3
    # 5


def fab2(max_n):
    n, a, b = 0, 0, 1
    while n < max_n:
        yield b
        a, b = b, a + b
        n += 1


def t4():
    for i in fab2(5):
        print i
    # 1
    # 1
    # 2
    # 3
    # 5


def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


def test():
    a = [1, 2, 4, 5]
    for i in a:
        yield i


def t5():
    for i in test():
        print i

if __name__ == '__main__':
    t5()
