

a = "dsd"
b = dict(a="aa")

print locals()
print globals()

# {'a': 'dsd', 'b': {'a': 'aa'}, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/root/github/python/dynamic/a.py', '__package__': None, '__name__': '__main__', '__doc__': None}
# {'a': 'dsd', 'b': {'a': 'aa'}, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/root/github/python/dynamic/a.py', '__package__': None, '__name__': '__main__', '__doc__': None}

locals()["a"] = "sss"
print a
locals()["b"]["a"] = "sss"
print b
# sss
# {'a': 'sss'}

# globals()["a"] = "sss"
# print a
# globals()["b"]["a"] = "sss"
# print b
# sss
# {'a': 'sss'}
