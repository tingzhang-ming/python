# encoding: utf-8
import os
from mockito import when, mock, unstub, any, verify


class Test(object):

    def test1(self, a, b="a"):
        return a + b


def t1():
    t = Test()
    when(t).test1(any(), b="heihei").thenReturn("bala")
    when(t).test1(any(), b="ha").thenReturn("bala222")
    print t.test1("1", b="heihei")
    print t.test1("1", b="ha")
# True


if __name__ == '__main__':
    t1()
    # clean up
    unstub()
