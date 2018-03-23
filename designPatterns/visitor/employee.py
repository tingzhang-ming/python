from abc import ABCMeta, abstractmethod


class Employee(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def accept(self, visitor):
        pass


class CommonEmployee(Employee):

    def __init__(self):
        self._job = None
        super(CommonEmployee, self).__init__()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job

    def accept(self, visitor):
        visitor.visit(self)


class Manager(Employee):

    def __init__(self):
        self._performance = None
        super(Manager, self).__init__()

    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, performance):
        self._performance = performance

    def accept(self, visitor):
        visitor.visit(self)

