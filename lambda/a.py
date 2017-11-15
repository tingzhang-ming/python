
def t1():
    f = lambda x,y,z:x+y+x
    print f(1,2,3)
    #4

def t2():
    f = lambda x,y,z:x+y+x, [1]
    print f()
    #4

if __name__ == '__main__':
    t2()