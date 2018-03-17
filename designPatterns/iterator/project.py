from abc import ABCMeta, abstractmethod


class AbstractProject(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, name, num, cost):
        pass

    @abstractmethod
    def get_project_info(self):
        pass

    @abstractmethod
    def get_iterator(self):
        pass


class Project(AbstractProject):

    def __init__(self, name, num, cost):
        self._name = name
        self._num = num
        self._cost = cost
        self._project_list = [self]

    def add(self, name, num, cost):
        self._project_list.append(Project(name, num, cost))

    def get_project_info(self):
        print "name is ", self._name
        print "num is ", self._num
        print "cost is ", self._cost

    def get_iterator(self):
        for i in self._project_list:
            yield i


if __name__ == '__main__':
    p = Project('p1', "1", "111")
    p.add('p2', '2', '222')
    p.add('p3', '3', '333')
    p.add('p4', '4', '444')
    for i in p.get_iterator():
        i.get_project_info()

# name is  p1
# num is  1
# cost is  111
# name is  p2
# num is  2
# cost is  222
# name is  p3
# num is  3
# cost is  333
# name is  p4
# num is  4
# cost is  444

