import asyncio
import functools


def hello_world():
    print('Hello world!')


def stop_loop(loop):
    print('Stopping loop.')
    loop.stop()


def t1():
    loop = asyncio.get_event_loop()
    print(loop.is_running())
    loop.call_soon(hello_world)
    loop.call_soon(functools.partial(stop_loop, loop))
    loop.run_forever()


@asyncio.coroutine
def coro_sum(*args):
    answer = 0
    for i in args:
        answer += i
    print(answer)
    return answer


def t2():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro_sum(1, 2, 3, 4, 5))
    # 15


@asyncio.coroutine
def nested(*args):
    print('The `nested` function ran with args: %r' % (args, ))
    return [i + 1 for i in args]


@asyncio.coroutine
def outer(*args):
    print('The `outer` function ran with args: %r' % (args,))
    answer = yield from nested(*[i * 2 for i in args])
    return answer


def t3():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(outer(2, 3, 5, 8))
# The `outer` function ran with args: (2, 3, 5, 8)
# The `nested` function ran with args: (4, 6, 10, 16)


@asyncio.coroutine
def make_tea(variety):
    print('Now making %s tea.' % variety)
    asyncio.get_event_loop().stop()
    return '%s tea' % variety


def t4():
    task = asyncio.ensure_future(make_tea('chamomile'))
    print(task.done())
    loop = asyncio.get_event_loop()
    loop.run_forever()
    print(task.done())
"""
False
Now making chamomile tea.
True
"""


@asyncio.coroutine
def make_tea(variety):
    print('Now making %s tea.' % variety)
    return '%s tea' % variety


def confirm_tea(future):
    print('The %s is made.' % future.result())


def t5():
    task = asyncio.ensure_future(make_tea('green'))
    task.add_done_callback(confirm_tea)
    print(task.done())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    print(task.done())
"""
False
Now making green tea.
The green tea is made.
True
"""


if __name__ == '__main__':
    t5()
