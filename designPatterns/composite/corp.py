

class Corp(object):

    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary

    def get_info(self):
        print "---name: %s----" % self._name
        print "position: ", self._position
        print "salary: ", self._salary


class Branch(Corp):

    def __init__(self, name, position, salary):
        super(Branch, self).__init__(name, position, salary)
        self.sub = []

    def add_sub(self, sub):
        self.sub.append(sub)

    def get_sub(self):
        return self.sub


def get_tree_info(root):
    for r in root.get_sub():
        if isinstance(r, Branch):
            r.get_info()
            get_tree_info(r)
        else:
            r.get_info()


def main():
    ceo = Branch("ceo_name", "ceo", 100000)
    l1 = Branch("haha", "leader1", 10000)
    l2 = Branch("haha2", "leader2", 10001)
    ceo.add_sub(l1)
    ceo.add_sub(l2)

    y1 = Corp("y1", "y1", 1)
    y2 = Corp("y2", "y2", 2)
    y3 = Corp("y3", "y3", 3)

    ceo.add_sub(y1)
    l1.add_sub(y2)
    l2.add_sub(y3)

    ceo.get_info()
    get_tree_info(ceo)


if __name__ == '__main__':
    main()

