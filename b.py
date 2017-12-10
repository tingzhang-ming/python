import os


def t1():
    a = "sdfdsf"
    b = a.encode('utf-8')
    print b


def t2():
    a = [2, 4, 1, 9, 8]
    a.sort()
    print a
    # [1, 2, 4, 8, 9]


def t3():
    a = ['test_9', 'test_4', 'test_6']
    a.sort()
    print a
    # ['test_4', 'test_6', 'test_9']


def t4():
    print os.listdir('./unittest')


def t5():
    print 14655800/1024/1024


def t6():
    a = ['mhc', 'mhc2']
    print " ".join(a)


def t7():
    a = 'mysql.ms.haha'
    a_split = a.split('.')
    a_len = len(a_split)
    for i in range(a_len):
        yield '.'.join(a_split[:i+1])


def t8():
    for i in t7():
        print i

if __name__ == '__main__':
    t8()
