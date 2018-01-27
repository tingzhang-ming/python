import asyncio


def t1():
    queue = asyncio.Queue()
    queue.put_nowait('foo')
    print(queue.qsize())
    print(queue.get_nowait())
    print(queue.qsize())


if __name__ == '__main__':
    t1()
