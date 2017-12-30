from datetime import datetime


class MyDate(datetime):
    def __format__(self, spec_str):
        if not spec_str:
            spec_str = '%Y-%m-%d %H:%M:%S'
        return self.strftime(spec_str)


def t1():
    md = MyDate(2012, 4, 21, 11)
    print '{0}'.format(md)
    print '{}'.format(md)
    print '{0:%Y-%m-%d}'.format(md)
"""
2012-04-21 11:00:00
2012-04-21 11:00:00
2012-04-21
"""


class Test(object):

    def __format__(self, spec_str):
        return spec_str


def t2():
    t = Test()
    print '{name:hahah}'.format(name=t)
    # hahah

if __name__ == '__main__':
    t2()
