import asyncio


async def nested(*args):
    print('The `nested` function ran with args: %r' % (args, ))
    return [i + 1 for i in args]


async def outer(*args):
    print('The `outer` function ran with args: %r' % (args,))
    answer = await nested(*[i * 2 for i in args])    # 异步调用， 执行时间较长的io
    print(answer)
    return answer


def t1():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(outer(2, 3, 5, 8))


if __name__ == '__main__':
    t1()
