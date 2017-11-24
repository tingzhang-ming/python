from module_test import Abstract_test1
from module_test2 import Abstract_test2


class Test(Abstract_test1, Abstract_test2):

    def __init__(self, name):
        Abstract_test1.__init__(self, name)
        Abstract_test2.__init__(self, name+"222")

    def get1(self):
        super(Test, self).get1()

    def get2(self):
        super(Test, self).get2()

    def set2(self, name):
        super(Test, self).set2(name)
        self.name = name

    def set1(self, name):
        super(Test, self).set1(name)
        self.name = name