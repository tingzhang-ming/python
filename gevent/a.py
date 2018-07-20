import os
from gevent import monkey
monkey.patch_socket()
import gevent
import urllib2


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i


def t1():
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()


def f2(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


def t2():
    gevent.joinall([
        gevent.spawn(f2, 'https://www.python.org/'),
        gevent.spawn(f2, 'https://www.baidu.com/'),
        gevent.spawn(f2, 'https://github.com/')
    ])


if __name__ == '__main__':
    t2()

