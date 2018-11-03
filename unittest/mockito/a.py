# encoding: utf-8
import os
from mockito import when, mock, unstub, any


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


if __name__ == '__main__':
    t2()
    # clean up
    unstub()
