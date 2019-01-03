# encoding: utf-8
"""
把类的类方法和静态方法注册成模块的函数
没有对实例方法进行过滤，所以被修饰的类里不要有实例方法
"""


def register(create_var=None):
    def wrapper(cls):
        if not create_var:
            return cls

        def apply_a(name):
            return lambda *args, **kwargs: apply(getattr(cls, name), args, kwargs)

        for k in vars(cls).keys():
            if '__' in k:
                continue
            create_var["a_" + k] = apply_a(k)
        return cls
    return wrapper
