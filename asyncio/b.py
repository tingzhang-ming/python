import asyncio
import functools


@asyncio.coroutine
def make_tea(variety):
    print('Now making %s tea.' % variety)
    return '%s tea' % variety


def t1():
    meta_task = asyncio.gather(
        make_tea('chamomile'),
        make_tea('green'),
        make_tea('herbal')
    )
    print(meta_task.done())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(meta_task)
    print(meta_task.done())
"""
False
Now making green tea.
Now making chamomile tea.
Now making herbal tea.
True
"""


@asyncio.coroutine
def make_tea(variety):
    print('Now making %s tea.' % variety)
    return '%s tea' % variety


def mix(future):
    print('Mixing the %s together.' % ' and '.join(future.result()))


def t2():
    meta_task = asyncio.gather(
        make_tea('chamomile'),
        make_tea('green'),
        make_tea('herbal')
    )
    meta_task.add_done_callback(mix)
    print(meta_task.done())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(meta_task)
    print(meta_task.done())
"""
False
Now making green tea.
Now making chamomile tea.
Now making herbal tea.
Mixing the chamomile tea and green tea and herbal tea together.
True
"""


def t3():
    coro = asyncio.wait([
        make_tea('chamomile'),
        make_tea('green'),
    ])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro)
"""
Now making chamomile tea.
Now making green tea.
"""


def t4():
    coro = asyncio.wait([
        asyncio.sleep(5),
        asyncio.sleep(1),
    ], timeout=3)
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(coro))

# ({<Task finished coro=<sleep() done, defined at /root/python3/lib/python3.6/asyncio/tasks.py:468> result=None>},
# {<Task pending coro=<sleep() running at /root/python3/lib/python3.6/asyncio/tasks.py:482> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7fc6d0ed6a68>()]>>})


def t5():
    coro = asyncio.wait([
        asyncio.sleep(3),
        asyncio.sleep(2),
        asyncio.sleep(1),
    ], return_when=asyncio.FIRST_EXCEPTION)   # asyncio.FIRST_COMPLETED
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(coro))


if __name__ == '__main__':
    t4()
