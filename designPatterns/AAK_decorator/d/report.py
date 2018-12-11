from abc import ABCMeta, abstractmethod
from types import MethodType
from functools import wraps


def high_score(func):
    @wraps(func)
    def new_method(self, *args, **kwargs):
        print "report high score"
        return func(self, *args, **kwargs)
    return new_method


def sort(func):
    @wraps(func)
    def new_method(self, *args, **kwargs):
        out = func(self, *args, **kwargs)
        print "report sort"
        return out
    return new_method

#############################################


class SchoolReport(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def sign(self):
        pass


class FourSchoolReport(SchoolReport):

    @high_score
    @sort
    def report(self):
        """
        report my score
        """
        print "report score"

    def sign(self):
        print "sign father name"


if __name__ == '__main__':
    sr = FourSchoolReport()
    sr.report()
    sr.sign()
    print(sr.report.__doc__.strip())


# report high score
# report score
# report sort
# sign father name
# report my score

