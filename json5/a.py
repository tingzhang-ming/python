import json5

a = "{timeout:0,databases:13}"
a= "{timeout:'q',databases:'a'}"

b = json5.loads(a)

print b