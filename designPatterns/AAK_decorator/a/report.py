from abc import ABCMeta, abstractmethod


class SchoolReport(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def sign(self):
        pass


class FourSchoolReport(SchoolReport):

    def report(self):
        print "report score"

    def sign(self):
        print "sign father name"

############################################


class AbstractDecorator(object):

    __metaclass__ = ABCMeta

    def __init__(self, sr):
        self._sr = sr

    def report(self):
        self._sr.report()

    def sign(self):
        self._sr.sign()


class HighScoreDecorator(AbstractDecorator):

    def _report_high_score(self):
        print "report high score"

    def report(self):
        self._report_high_score()
        super(HighScoreDecorator, self).report()


class SortDecorator(AbstractDecorator):

    def _report_sort(self):
        print "report sort"

    def report(self):
        super(SortDecorator, self).report()
        self._report_sort()


if __name__ == '__main__':
    sr = FourSchoolReport()
    sr = HighScoreDecorator(sr)
    sr = SortDecorator(sr)

    sr.report()
    sr.sign()

# report high score
# report score
# report sort
# sign father name

