import asyncio


def f1():
    a = [1, 2, 3, 4, 5]
    yield from a


def t1():
    for i in f1():
        print(i)


@asyncio.coroutine
def f2():
    a = [1, 2, 3, 4, 5]
    print(a)
    return a


@asyncio.coroutine
def t2():
    b = yield from f2()
    print(b)
    return b


def t3():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(t2())


if __name__ == '__main__':
    t3()
