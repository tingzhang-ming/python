from copy import copy


def t1():
    a = []
    if a:
        print "not empty"
    else:
        print "empty or none"


def t2():
    a = ["a", "b", "c"]
    print a.index("a")
    print a.index("d")


def merge_list(list1, list2):
    res = copy(list1)
    res.extend(list2)
    return res


def t3():
    a = ["1", "2"]
    b = ["3", "4"]
    c = merge_list(a, b)
    print c
    a.append("sfsdf")
    print a
    print c


def t4():
    a = [1, 2, 3, 4]
    print a[0:-1]
# [1, 2, 3]


if __name__ == '__main__':
    t4()
