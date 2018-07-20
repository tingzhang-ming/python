# encoding: utf-8
import time
# 监控文件的内容增加


def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(1)
            continue
        print "get"
        target.send(line)


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start


@coroutine
def printer():
    while True:
        line = (yield)
        print line


if __name__ == '__main__':
    try:
        with open('/root/github/python/s3_test/test.txt') as f:
            follow(f, printer())
    except KeyboardInterrupt:
        print "exit"
