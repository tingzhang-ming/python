import memcache
# pip install python-memcached


def t1():
    mc = memcache.Client(['ali:11211'], debug=True)
    mc.set("name", "python")
    ret = mc.get("name")
    print(ret)


def t2():
    mc = bmem
    mc.set("name", "python")
    ret = mc.get("name")
    print(ret)


if __name__ == '__main__':
    t1()
