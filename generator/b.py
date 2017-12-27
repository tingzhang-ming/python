

def squares():
    cursor = 1
    while True:
        yield cursor ** 2
        cursor += 1


def t1():
    for i in squares():
        print i
        if i > 100:
            break
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121


def squares2(cursor=1):
    while True:
        response = yield cursor ** 2
        if response:
            print "response: %s" % response
            cursor = response
        else:
            cursor += 1


def t2():
    sq = squares2()
    print next(sq)
    print next(sq)
    print sq.send(7)
    print next(sq)
    print next(sq)
# 1
# 4
# response: 7
# 49
# 64
# 81


def squares3(cursor=1):
    response = None
    while True:
        if response:
            print "response: %s" % response
            response = yield response ** 2
            continue
        response = yield cursor ** 2
        cursor += 1
# 1
# 4
# response: 7
# 49
# 9
# 16


def t3():
    sq = squares3()
    print next(sq)
    print next(sq)
    print sq.send(7)
    print next(sq)
    print next(sq)



if __name__ == '__main__':
    t3()
