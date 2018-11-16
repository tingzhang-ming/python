# encoding: utf-8
import os
from mockito import when, mock, unstub, any, verify


def t1():
    when(os.path).exists('/foo').thenReturn(True)
    print os.path.exists('/foo')
# True


def t2():
    # or:
    import requests  # the famous library
    # you actually want to return a Response-like obj, we'll fake it
    response = mock({'status_code': 200, 'text': 'Ok'})
    when(requests).get(any()).thenReturn(response)   # python3 里将any()换成...

    # use it
    res = requests.get('http://google.com/')
    print res.status_code
    print res.text
# 200
# Ok


class Manager(object):

    def add_tasks(self, a, b, c):
        pass


# must use 'when' first
def t3():
    manager = Manager()
    when(manager).add_tasks(any(), any(), any())
    manager.add_tasks(1, 2, 4)
    verify(manager).add_tasks(1, 2, 3)
# Wanted but not invoked:  add_tasks(1, 2, 3)
# Instead got:             [add_tasks(1, 2, 4)]


if __name__ == '__main__':
    t3()
    # clean up
    unstub()
