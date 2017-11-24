import string

def t1():
    # a = {"a","b", [1,2,3]}
    b = ("a","b",[1,2,3])
    print b

def t2():
    a = ["aaa","ssd"]
    b = string.join(a, ",")
    print b

def t3():
    a = [1,2,3,4]
    print a[1:]

def t4():
    a = 4096
    l = ["q","w","e"]
    b = a/len(l)
    res = {ll:b for ll in l}
    c = a - b*len(l)
    res[l[0]] += c
    print res
    sum = 0
    for k, v in res.items():
        sum += v
    print sum

def t5():
    d = dict(
        n1="haha",
        n2="lala"
    )
    a = "asddasd--%(n1)s,asddff--%(n2)ssdfjdfhj--%(n1)s" %d
    print a

import os
def t6():
    a = [1,2,3,4,5]
    for k, v in enumerate(a):
        print k, v

if __name__ == '__main__':
    t6()