# encoding: utf-8


def t1():
    print ~5
    print ~(-5)
    # -6
    # 4
    # ~0 101 = 1 010 -> 1 001 -> 0110  # 减一, 取反
    # 0 101 -> 1 010 -> 1 011  ==  -5  # 取反, 加一
    # ~1 011 = 0 100  == 4


if __name__ == '__main__':
    t1()