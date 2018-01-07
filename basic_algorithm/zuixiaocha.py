from random import randrange

seq = [randrange(10**10) for i in range(100)]

dd = float("inf")
xx, yy = 0, 0
for x in seq:
    for y in seq:
        if x == y:
            continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d

print xx, yy

dd = float("inf")
xx, yy = 0, 0
seq.sort()
for i in range(len(seq)-1):
    d = abs(seq[i] - seq[i-1])
    if d < dd:
        xx, yy, dd = seq[i], seq[i-1], d
print xx, yy

