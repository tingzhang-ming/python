import re


def t1():
    patt = '\w+@(\w+\.)?\w+\.com'
    m = re.match(patt, 'nobody@xxx.com')
    if m is not None:
        print m.group()
        print m.groups()
    else:
        print m
    m = re.match(patt, 'nobody@www.xxx.com')
    if m is not None:
        print m.group()
        print m.groups()
    else:
        print m
    # nobody @ xxx.com
    # (None,)
    # nobody @ www.xxx.com
    # ('www.',)


if __name__ == '__main__':
    t1()
