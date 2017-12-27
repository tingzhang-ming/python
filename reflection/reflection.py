# coding: UTF-8
import sys  # 模块，sys指向这个模块对象
import inspect


def foo(): pass  # 函数，foo指向这个函数对象


class Cat(object):  # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!'  # 访问名为name的字段，使用实例.name访问


cat = Cat()  # cat是Cat类的实例对象

print Cat.sayHi  # 使用类名访问实例方法时，方法是未绑定的(unbound)  <unbound method Cat.sayHi>
print cat.sayHi  # 使用实例访问实例方法时，方法是绑定的(bound) <bound method Cat.sayHi of <__main__.Cat object at 0x7fcf16031110>>

print "-----------------------------------------------------------------"

cat = Cat('kitty')

print cat.name  # 访问实例属性
cat.sayHi()  # 调用实例方法

print dir(cat)  # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'):  # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger')  # same as: a.name = 'tiger'
print getattr(cat, 'name')  # same as: print a.name

getattr(cat, 'sayHi')()  # same as: cat.sayHi()

"""
kitty
kitty says Hi!
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'sayHi']
tiger
tiger says Hi!
"""
print "-----------------------------------------------------------------"

import fnmatch as m
print m.__doc__.splitlines()[0] # Filename matching with shell patterns.
print m.__name__                # fnmatch
print m.__file__                # /usr/lib64/python2.7/fnmatch.pyc
print m.__dict__.items()[0]     # ('_purge', <function _purge at 0x7f1df61e02a8>)

print "---------------------------------------------------------------------"

print Cat.__doc__           # None
print Cat.__name__          # Cat
print Cat.__module__        # __main__
print Cat.__bases__         # (<type>,)
print Cat.__dict__          # {'__module__': '__main__', ...}</type>

print "-------------------------------------------------------------------------"

print cat.__dict__         #{'name': 'tiger'}
print cat.__class__        #<class '__main__.Cat'>
print cat.__class__ == Cat # True

print "----------------------------------------------------------------------------"


def foo():
    n = 1

    def bar():
        print n  # 引用非全局的外部变量n，构造一个闭包

    n = 2
    return bar


closure = foo()
print closure.func_closure
print dir(closure.func_closure[0])
# ['__class__', '__cmp__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']
# 使用dir()得知cell对象有一个cell_contents属性可以获得值
print closure.func_closure[0].cell_contents  # 2

print "---------------------------------------------------------------------------"

im = cat.sayHi
print im.im_func #<function sayHi at 0x7ff6cec8a2a8>
print im.im_self # <__main__.Cat object at 0x7ff6cec9e7d0>
print im.im_class # <class '__main__.Cat'>

im.im_func(im.im_self) #tiger says Hi!

print "----------------------------------------------------------------------------"

def gen():
    for n in xrange(5):
        yield n
g = gen()
print g             # <generator object gen at 0x7f2a3ed8f0f0>
print g.gi_code     # <code object gen at 0x7f2a465f3330, file "/root/github/python/reflection/reflection.py", line 96>
print g.gi_frame    # <frame object at 0x...>
print g.gi_running  # 0
print g.next()      # 0
print g.next()      # 1
for n in g:
    print n,        # 2 3 4