from abc import ABCMeta, abstractmethod
from employee import CommonEmployee, Manager


class AbstractVisitor(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def visit(self, employee):
        pass


class Visitor(AbstractVisitor):

    def visit(self, employee):
        if isinstance(employee, CommonEmployee):
            print self._get_commone_info(employee)
        elif isinstance(employee, Manager):
            print self._get_mamanger_info(employee)
        else:
            print "unknown employee type"

    @staticmethod
    def _get_basic_info(employee):
        return "name is: %s" % (employee.name)

    def _get_mamanger_info(self, employee):
        return "%s\tperformance: %s" % (self._get_basic_info(employee), employee.performance)

    def _get_commone_info(self, employee):
        return "%s\tjob: %s" %(self._get_basic_info(employee), employee.job)


if __name__ == '__main__':
    c = CommonEmployee()
    c.name = "haha"
    c.job = "job1"

    m = Manager()
    m.name = "lala"
    m.performance = "good"

    v = Visitor()

    c.accept(v)
    m.accept(v)
# name is: haha	job: job1
# name is: lala	performance: good
