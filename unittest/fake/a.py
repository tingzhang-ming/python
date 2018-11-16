from fake import Fake


def t1():
    f = Fake()
    f.a = "haha"
    f.b = 222
    print f.a
    print f.b
    print f["a"]
    print f["b"]
    print f.to_dict()
    f["c"] = "ha"
    print f.to_dict()
    print f.c
# haha
# 222
# haha
# 222
# {'a': 'haha', 'b': 222}
# {'a': 'haha', 'c': 'ha', 'b': 222}
# ha


if __name__ == '__main__':
    t1()
