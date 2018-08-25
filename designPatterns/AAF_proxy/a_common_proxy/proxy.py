from gamePlayer import AbstractGamePlayer
from gamePlayer.player import Player


class PlayerProxy(AbstractGamePlayer):

    def __init__(self, name):
        try:
            self.game_player = Player(self, name)
        except Exception as e:
            print "error: {}".format(e.message)

    def login(self, user, password):
        self.game_player.login(user, password)

    def kill_boss(self):
        self.game_player.kill_boss()

    def upgrade(self):
        self.game_player.kill_boss()
