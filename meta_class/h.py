class A(object):

    def __init__(self):
        self.a = 999


mc = type(A)

print mc

cls = mc("B", (A,), {})

b = cls()

print b.a