

class Father(object):

    def __init__(self, name):
        self.name = name

    def get(self):
        print self.name

    def set(self, new):
        self.name = new


class Son(Father):

    def __init__(self, name):
        super(Son, self).__init__(name)
        self.son = "ha"

    def set(self, new):
        self.name = new+"222"

    def set2(self, new):
        super(Son, self).set(new)


if __name__ == '__main__':

    s = Son("mhc")
    s.get()
    s.set2("mhc111")
    s.get()