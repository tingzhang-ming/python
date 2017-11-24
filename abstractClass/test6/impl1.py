from abstract_class import Abstract_test


class Test(Abstract_test):

    def method1(self, name):
        print "hello", name

    def method2(self, name):
        super(Test, self).method2(name)
        print "i am method 2"
