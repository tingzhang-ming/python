

def is_odd(n):
    return n % 2 == 1


def t1():
    data = [1, 2, 3, 4, 5, 6]
    print(list(filter(lambda x: x % 2 == 1, data)))
# [1, 3, 5]


if __name__ == '__main__':
    t1()
