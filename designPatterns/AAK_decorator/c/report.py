from abc import ABCMeta, abstractmethod
from types import MethodType
from functools import wraps


class MethodNotExistException(Exception):
    def __init__(self, method_name, cls):
        super(MethodNotExistException, self).__init__("method '%s' not found in class" %method_name, cls)


class Decorator(object):

    def __init__(self, name):
        self._method_name = name

    def __call__(self, cls):
        if not (hasattr(cls, self._method_name) and isinstance(getattr(cls, self._method_name), MethodType)):
            raise MethodNotExistException(self._method_name, cls)
        origin_method = getattr(cls, self._method_name)
        new_method = self.custom(origin_method, cls)
        setattr(cls, self._method_name, new_method)
        return cls

    def custom(self, origin_method, cls):
        @wraps(origin_method)
        def new_method(self, *args, **kwargs):
            origin_method(self, *args, **kwargs)
        return new_method


class HighScoreDecorator(Decorator):

    def __init__(self):
        super(HighScoreDecorator, self).__init__("report")

    def custom(self, origin_method, cls):
        @wraps(origin_method)
        def new_method(self, *args, **kwargs):
            print "report high score"
            origin_method(self, *args, **kwargs)
        return new_method


class SortDecorator(Decorator):
    def __init__(self):
        super(SortDecorator, self).__init__("report")

    def custom(self, origin_method, cls):
        @wraps(origin_method)
        def new_method(self, *args, **kwargs):
            origin_method(self, *args, **kwargs)
            print "report sort"
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


@HighScoreDecorator()
@SortDecorator()
class FourSchoolReport(SchoolReport):

    def report(self):
        """
        report my score222
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
# report my score222

