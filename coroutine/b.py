import time


def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
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
    with open('/root/github/python/s3_test/test.txt') as f:
        follow(f, printer())
