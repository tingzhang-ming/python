from functools import wraps
from gamePlayer import AbstractGamePlayer
from proxy import PlayerProxy


def decorator(fun):
    @wraps(fun)
    def inner(cls, *args, **kwargs):
        if not cls.proxy:
            print "Please set proxy"
            return
        return fun(cls, *args, **kwargs)
    return inner


class Player(AbstractGamePlayer):

    def __init__(self, name):
        self.proxy = None
        self.name = name

    @decorator
    def login(self, user, password):
        print "login user: %s, password: %s" % (user, password)

    @decorator
    def kill_boss(self):
        print "{} kill boss".format(self.name)

    @decorator
    def upgrade(self):
        print "{} upgrade".format(self.name)

    def get_proxy(self):
        self.proxy = PlayerProxy(self)

    def is_proxy(self):
        return self.proxy is not None

