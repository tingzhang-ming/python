

def is_odd(n):
    return n % 2 == 1


def t1():
    data = [1, 2, 3, 4, 5, 6]
    print(list(filter(lambda x: x % 2 == 1, data)))
# [1, 3, 5]


def t11():
    a = [1, 4, 6, 7, 9, 12, 17]
    print filter(is_odd, a)
# [1, 7, 9, 17]


def t2():
    a = [1, 4, 6, 7, 9, 12, 17]
    print filter(lambda x: x % 2 == 1, a)
# [1, 7, 9, 17]


if __name__ == '__main__':
    t1()
