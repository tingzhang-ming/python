

def f(x):
    return x * x


def t1():
    a = [1, 2, 3, 4]
    for i in map(f, a):
        print(i)
# 1
# 4
# 9
# 16


def t2():
    a = [1, 2, 3, 4]
    print(list(map(str, a)))
# ['1', '2', '3', '4']


if __name__ == '__main__':
    t1()
