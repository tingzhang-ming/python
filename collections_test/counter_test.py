from collections import Counter


def t1():
    c = Counter('aabcdefff')
    print c['a']
    print c['b']
    print c
    print c['f']
    print c['g']
    # 2
    # 1
    # Counter({'f': 3, 'a': 2, 'c': 1, 'b': 1, 'e': 1, 'd': 1})
    # 3
    # 0


def t2():
    c = Counter({'a': 4, 'b': 2})
    print c
    print c['a']
    # Counter({'a': 4, 'b': 2})
    # 4


def t3():
    c = Counter(a=4, b=2)
    print c
    print c['a']
    # Counter({'a': 4, 'b': 2})
    # 4


def t4():
    c = Counter('aabcdefff')
    print c['a']
    c.update('ha')
    print c['a']
    print c['h']
    # 2
    # 3
    # 1


def t5():
    c = Counter('aabcdefff')
    print c['a']
    c.subtract('ha')
    print c['a']
    print c['h']
    # 2
    # 1
    # -1


def t6():
    c = Counter('aabcdefff')
    print c
    del c['a']
    print c
    # Counter({'f': 3, 'a': 2, 'c': 1, 'b': 1, 'e': 1, 'd': 1})
    # Counter({'f': 3, 'c': 1, 'b': 1, 'e': 1, 'd': 1})


def t7():
    c = Counter('aabcdefff')
    print list(c.elements())
    # ['a', 'a', 'c', 'b', 'e', 'd', 'f', 'f', 'f']  wu xu


def t8():
    c = Counter('aabcdefff')
    print c.most_common()
    print c.most_common(2)
    # [('f', 3), ('a', 2), ('c', 1), ('b', 1), ('e', 1), ('d', 1)]
    # [('f', 3), ('a', 2)]


def t9():
    a = Counter(a=1, b=2)
    b = Counter(a=2, b=1)
    print a + b
    print a - b
    print a & b
    print a | b
    # Counter({'a': 3, 'b': 3})
    # Counter({'b': 1})
    # Counter({'a': 1, 'b': 1})
    # Counter({'a': 2, 'b': 2})

if __name__ == '__main__':
    t9()
