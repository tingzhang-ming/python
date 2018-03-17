
def t1():
    s = 9999999999
    print 0x7fffffff
    print s & 0x7fffffff


def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


if __name__ == '__main__':
    t1()
