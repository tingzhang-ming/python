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


def _parse_uri(uri):
    """ parse download uri """
    if "ftp://" in uri:
        url = string.lstrip(uri, "ftp://")
    elif "http://" in uri:
        url = string.lstrip(uri, "http://")
    elif "manta://" in uri:
        url = string.lstrip(uri, "manta://")
    else:
        raise Exception("Expecting 'ftp://' or 'http://' at the beginning of the URL")
    try:
        file_name = uri.split("/")[-1]
    except ValueError:
        raise Exception("can not get file name from %s" % uri)
    return file_name


def t7():
    u = "manta://test1-mysql-dump-2017-11-28T03-08-49Z.gz"
    print _parse_uri(u)


def _explodeLocation(location):
    storage_url = "/".join(location.split('/')[:-2])
    container = location.split('/')[-2]
    filename = location.split('/')[-1]
    return storage_url, container, filename


def t8():
    location = "/backup/location/123"
    print _explodeLocation(location)

if __name__ == '__main__':
    t8()
