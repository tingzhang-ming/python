

def t1():
    a = {}
    a['a1'] = "dsadfsf"
    a['a2'] = ["dfsdf"]
    for k,v in a.items():
        exec("{}={}".format(k, v))
    print a1
    print a2


if __name__ == '__main__':
    t1()
