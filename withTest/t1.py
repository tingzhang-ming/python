
class Test(object):

    def __init__(self):
        self.a = "hahahah"

    def __enter__(self):
        print "enter------------"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "exit-----------------"
        print exc_type
        print exc_val
        print exc_tb


def t1():
    with Test() as f:
        print f.a


def t2():
    with Test():
        print "hahah"
        raise KeyError("sadasfdsf")
# enter------------
# hahah
# exit-----------------
# <type 'exceptions.KeyError'>
# 'sadasfdsf'
# <traceback object at 0x7fee8b0d6e60>

if __name__ == '__main__':
    t1()
