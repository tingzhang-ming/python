import foo

print dir(foo)
print foo.__doc__
print foo.bar2(1, 2.0, "haha")
print foo.bar3(1, 2.0, "haha")
print foo.bar3(1, 2.0, "haha", 200)
print foo.bar4(i=1, d=2.0, s="haha")
print foo.add_sub(2, 5)

# ['__doc__', '__file__', '__name__', '__package__', 'add_sub', 'bar', 'bar2', 'bar3', 'bar4']
# My first extension module.
# iNum: 1, fNum: 2.000000, str: haha
# None
# iNum: 1, fNum: 2.000000, str: haha, iNum2: 4, fNum2: 5.000000, str2: hello,
# None
# iNum: 1, fNum: 2.000000, str: haha, iNum2: 200, fNum2: 5.000000, str2: hello,
# None
# num is: 1,2.000000,haha
# None
# (7, -3)

