

class A(object):

    r = ["a1", "a2"]
    o = ["a3"]

    @classmethod
    def val(cls):
        print str(cls.r)
        print str(cls.o)


class B(A):

    r = A.r + ["b1"]
    o = A.o + ["b2"]


class C(B):

    @classmethod
    def val(cls):
        super(C, cls).val()
        print "ccc"


if __name__ == '__main__':
    B.val()
    C.val()
