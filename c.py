import os
import sys


def t1():
    path = '/root/github/ConductorWorker/mworker/dbcmft/handler.py'
    print sys.path
    path_dir = os.path.dirname(path)
    if path_dir not in sys.path:
        sys.path.append(path_dir)
    handler = __import__('handler', fromlist=path_dir)
    print handler.test_task({"inputData": "hahah"})


def t2():
    a = {}
    try:
        print a['a']
    except Exception as e:
        print e.__class__.__name__


def t3():
    jf = 'ms.json'
    print jf.split('.json')[0]


def t4():
    sys.stderr.write('hahaha')
    sys.stderr.write('hahaha2')


if __name__ == '__main__':
    t4()

