from functools import reduce


def t1():
    print(reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9]))
# 13579


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int(text):
    return reduce(lambda x, y: x * 10 + y, map(char2num, text))


def t2():
    print(str2int("123434344"))
# 123434344


if __name__ == '__main__':
    t2()
