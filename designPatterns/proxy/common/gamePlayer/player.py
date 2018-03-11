from gamePlayer import AbstractGamePlayer


class Player(AbstractGamePlayer):

    def __init__(self, proxy, name):
        if not issubclass(type(proxy), AbstractGamePlayer):
            raise Exception("can not create real player")
        self.name = name

    def login(self, user, password):
        print "login user: %s, password: %s" % (user, password)

    def kill_boss(self):
        print "{} kill boss".format(self.name)

    def upgrade(self):
        print "{} upgrade".format(self.name)
