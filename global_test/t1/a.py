from register import register


_create_var = locals()


@register(create_var=_create_var)
class A(object):

    @classmethod
    def t1(cls):
        print "t1"

    @classmethod
    def t2(cls):
        cls.t1()
        print "t2"

    @classmethod
    def t3(cls, t):
        print t
        cls.t1()




a_t3("sfsdf")




