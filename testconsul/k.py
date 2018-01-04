import os
import time
from threading import Thread
from tornado.ioloop import IOLoop
from tornado.gen import coroutine
from consul.base import Timeout
from consul.tornado import Consul

os.environ['http_proxy'] = ''


class Msg(object):

    def __init__(self):
        self.foo = None


class Config(object):
    def __init__(self, loop1, msg):
        self.msg = msg
        loop1.add_callback(self.watch)

    @coroutine
    def watch(self):

        c = Consul()

        # asynchronously poll for updates
        index = None
        while True:
            try:
                index, data = yield c.kv.get('mhc', index=index)
                if data is not None:
                    self.msg.foo = data['Value']
            except Timeout:
                # gracefully handle request timeout
                pass


def work(msg):
    while True:
        print msg.foo
        time.sleep(3)

if __name__ == '__main__':
    loop = IOLoop.instance()
    msg = Msg()
    wt = Thread(target=work, args=(msg,))
    wt.setDaemon(True)
    wt.start()
    _ = Config(loop, msg)
    loop.start()

