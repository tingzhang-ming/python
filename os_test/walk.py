import os


def t1():
    path = "D:\github\conductor-dev\python\conductor-worker\workers"
    for root, _, files in os.walk(path):
        print "root: %s" % root
        print "files: %s" % str(files)


if __name__ == '__main__':
    t1()
