import bypy


bp = bypy.ByPy()


def t1():
    for i in range(1001):
        with open('/tmp/bypy.txt', 'w') as f:
            f.write(str(i))
        bp.upload('/tmp/bypy.txt', 'mhc/test-{}.txt'.format(str(i)))


if __name__ == '__main__':
    t1()
