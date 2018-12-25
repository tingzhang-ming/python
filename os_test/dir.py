import os
from twitter.common.dirutil import safe_mkdir


def t1():
    os.mkdir("/etc/a")


def t2():
    safe_mkdir("/etc/a/b/c/e/d")


if __name__ == '__main__':
    t2()
