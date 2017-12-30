import os
import tempfile
import shutil


def t1():
    a = tempfile.mkdtemp()
    print a


class TempDirectory(object):

    def __init__(self):
        self.tmp_dir = None

    def __enter__(self):
        self.tmp_dir = tempfile.mkdtemp()
        return self.tmp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.tmp_dir)


def t2():
    with TempDirectory() as t:
        print t
        with open(os.path.join(t, 'aa'), 'w') as f:
            f.write('dsfsdgdfgsdfg')
        print os.path.isdir(t)
    print os.path.isdir(t)


def t3():
    a = tempfile.mkdtemp(dir='/root')
    print a

if __name__ == '__main__':
    t3()
