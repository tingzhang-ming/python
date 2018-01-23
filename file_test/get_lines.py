from queue import Queue


def get_file_count(path='/root/github/python/s3_test/test.txt'):
    n = 5
    q = []
    with open(path, 'rU') as f:
        for count, line in enumerate(f):
            add_que(q, line, n)
    res = ''
    for i in q:
        res += i
    return res


def add_que(que, item, maxsize):
    if len(que) == maxsize:
        que.pop(0)
    que.append(item)


def t1():
    q = []
    add_que(q, 1, 2)
    add_que(q, 2, 2)
    add_que(q, 3, 2)
    add_que(q, 4, 2)
    print q.pop(0)
    print q.pop(0)




if __name__ == '__main__':
    print get_file_count()
