from abstract_game_player import AbstractGamePlayer
from proxy import ProxyFactory, InvocationHandler


class MyInvocationHandler(InvocationHandler):

    def __call__(self, *args, **kwargs):
        if self.func.__name__ == 'login':
            print("someone login my account")
        return self.func(*args, **kwargs)


@ProxyFactory(MyInvocationHandler)
class Player(AbstractGamePlayer):

    def __init__(self, name):
        self.proxy = None
        self.name = name

    def login(self, user, password):
        print "login user: %s, password: %s" % (user, password)

    def kill_boss(self):
        print "{} kill boss".format(self.name)

    def upgrade(self):
        print "{} upgrade".format(self.name)


if __name__ == '__main__':
    p = Player("mhc")
    p.login("user", "name")
    p.kill_boss()
    p.upgrade()
    p.login("user2", "name2")

# someone login my account
# login user: user, password: name
# mhc kill boss
# mhc upgrade

