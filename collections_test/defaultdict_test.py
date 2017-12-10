from collections import defaultdict


def t1():
    strings = ('a', 'b', 'c', 'a')
    counts = {}
    for kw in strings:
        if kw not in counts:
            counts[kw] = 1
        else:
            counts[kw] += 1
    print counts
    # {'a': 2, 'c': 1, 'b': 1}


def t2():
    strings = ('a', 'b', 'c', 'a')
    counts = {}
    for kw in strings:
        counts.setdefault(kw, 0)
        counts[kw] += 1
    # for kw in strings:
    #     counts[kw] = counts.setdefault(kw, 0) + 1
    print counts
    # {'a': 2, 'c': 1, 'b': 1}


def t3():
    strings = ('a', 'b', 'c', 'a')
    counts = defaultdict(int)
    for kw in strings:
        counts[kw] += 1
    print counts
    # defaultdict(<type 'int'>, {'a': 2, 'c': 1, 'b': 1})


if __name__ == '__main__':
    t3()
