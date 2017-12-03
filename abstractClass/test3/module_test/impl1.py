from module_test import Abstract_test


class Test(Abstract_test):

    def __init__(self, name):
        super(Test, self).__init__(name)

    def get(self):
        super(Test, self).get()

    def set(self, name):
        super(Test, self).set(name)
        self.name = name

    def p(self):
        print self.name
        print self.name2
