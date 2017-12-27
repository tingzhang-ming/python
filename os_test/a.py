import os

def t1():
    a = os.path.expanduser("~/a/b")
    print a

# /root/a/b

def t2():
    a = os.path.expandvars("$PATH")
    print a

# /root/packet/go/bin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/root/bin

if __name__ == '__main__':
    t2()