import os
a = "a"

b = a
l = []
while b != "/":
    b = os.path.dirname(b)
    print b
    if not b:
        break
    l.append(b)

# l = list(reversed(l))
# l.append(a)
# for ll in l:
#     if not os.path.exists(ll):
#         os.mkdir(ll)