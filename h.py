

def t1():
    for i in range(10):
        print i
        i = i+1


def t2():
    a = {
        "a": 1,
        "b": 2,
    }
    print a
    a.pop("a")
    print a
# {'a': 1, 'b': 2}
# {'b': 2}


if __name__ == '__main__':
    t2()
