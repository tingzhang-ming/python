import test1

print test1.__dict__.keys()
print dir(test1)
print vars(test1).keys()

"""
['__builtins__', '__file__', '__doc__', '__name__', '__package__', 'hello']
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'hello']
['__builtins__', '__file__', '__doc__', '__name__', '__package__', 'hello']
"""