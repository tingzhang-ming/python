from abc import ABCMeta, abstractmethod
from types import MethodType
from functools import wraps


def high_score(cls):
    if not (hasattr(cls, "report") and isinstance(getattr(cls, "report"), MethodType)):
        return cls
    origin_method = getattr(cls, "report")
    @wraps(origin_method)
    def new_method(self, *args, **kwargs):
        print "report high score"
        origin_method(self, *args, **kwargs)
    setattr(cls, "report", new_method)
    return cls


def sort(cls):
    if not (hasattr(cls, "report") and isinstance(getattr(cls, "report"), MethodType)):
        return cls
    origin_method = getattr(cls, "report")
    @wraps(origin_method)
    def new_method(self, *args, **kwargs):
        origin_method(self, *args, **kwargs)
        print "report sort"
    setattr(cls, "report", new_method)
    return cls

#############################################


class SchoolReport(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def sign(self):
        pass


@high_score
@sort
class FourSchoolReport(SchoolReport):

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

