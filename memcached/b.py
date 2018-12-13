import bmemcached


def t1():
    client = bmemcached.Client(['ali:11211'], 'mhc', 'mhc.123')
    client.set("name", "test")
    res = client.get("name")
    print(res)


if __name__ == '__main__':
    t1()
