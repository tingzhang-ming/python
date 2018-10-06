import foo

print dir(foo)
print foo.__doc__
print foo.bar()

# ['__doc__', '__file__', '__name__', '__package__', 'bar']
# My first extension module.
# None