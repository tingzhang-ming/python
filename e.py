

def t1():
    a = [2, 3, 1]
    i = 0
    print a[:i+1]
    tmp = a[i+1:]
    tmp.reverse()
    print tmp
    print a
    print a[:i+1].extend(tmp)


if __name__ == '__main__':
    t1()

