

a = {'a': 1}


def t1():
    try:
        b = a['b']
    except IndexError:
        print 'key error'
        return
    finally:
        a.clear()



if __name__ == '__main__':
    t1()
    print a
