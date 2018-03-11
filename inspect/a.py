# -*- coding: utf-8 -*-
import inspect

import os


class Test(object):
    """Test Class """

    def test(self):
        self.fuc = lambda x: x


class Testone(Test):
    pass


def t1():
    # 检查类型，模块，类，方法，生成器，代码等都可以
    print inspect.ismodule(os)
    print inspect.isclass(Test)

    print inspect.getdoc(Test)
    print inspect.getsourcefile(Test)  # 文件路径
    print inspect.getsourcelines(Test)  # 代码块，每行一个元素，组成数组
    print "-" * 30
    print inspect.getsource(Test)  # 代码块 带缩进

# True
# True
# Test Class
# /root/github/python/inspect/a.py
# (['class Test(object):\n', '    """Test Class """\n', '\n', '    def test(self):\n', '        self.fuc = lambda x: x\n'], 7)
# ------------------------------
# class Test(object):
#     """Test Class """
#
#     def test(self):
#         self.fuc = lambda x: x


def t2():
    ##打印全局变量中的模块对象
    print "-" * 30
    myglobals = {}
    myglobals.update(globals())
    modules = [value
               for key, value in myglobals.items()
               if inspect.ismodule(value)]
    print modules
    """
    [<module '__builtin__' (built-in)>, <module 'inspect' from '/usr/lib64/python2.7/inspect.pyc'>, <module 'os' from '/usr/lib64/python2.7/os.pyc'>]
    """


def t3():
    ##查看类的可调用方法
    for name, value in inspect.getmembers(Test, callable):
        print "    Callable:", name

    for name, value in inspect.getmembers(Test(), callable):
        print "   Instance Callable:", name
    print "=" * 30

"""
    Callable: __class__
    Callable: __delattr__
    Callable: __format__
    Callable: __getattribute__
    Callable: __hash__
    Callable: __init__
    Callable: __new__
    Callable: __reduce__
    Callable: __reduce_ex__
    Callable: __repr__
    Callable: __setattr__
    Callable: __sizeof__
    Callable: __str__
    Callable: __subclasshook__
    Callable: test
   Instance Callable: __class__
   Instance Callable: __delattr__
   Instance Callable: __format__
   Instance Callable: __getattribute__
   Instance Callable: __hash__
   Instance Callable: __init__
   Instance Callable: __new__
   Instance Callable: __reduce__
   Instance Callable: __reduce_ex__
   Instance Callable: __repr__
   Instance Callable: __setattr__
   Instance Callable: __sizeof__
   Instance Callable: __str__
   Instance Callable: __subclasshook__
   Instance Callable: test
"""


def t4():
    print inspect.stack()[0][3]
    for i in inspect.stack():
        print i
# (<frame object at 0xc8a9d0>, '/root/github/python/inspect/a.py', 101, 't4', ['    for i in inspect.stack():\n'], 0)
# (<frame object at 0xbf45a0>, '/root/github/python/inspect/a.py', 106, '<module>', ['    t4()\n'], 0)


if __name__ == '__main__':
    t4()
