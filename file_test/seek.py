import time


def t1():
    f = open('/root/github/python/s3_test/test.txt')
    f.seek(0, 0)
    print f.readline()

    f.close()


def t2():
    f = open('/root/github/python/s3_test/test.txt', 'ra')
    f.seek(0, 2)
    # time.sleep(10)
    print f.readline()

    f.close()


if __name__ == '__main__':
    t2()
