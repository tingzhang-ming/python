from gamePlayer import AbstractGamePlayer


class PlayerProxy(AbstractGamePlayer):

    def __init__(self, game_player):
        self.game_player = game_player

    def login(self, user, password):
        self.game_player.login(user, password)

    def kill_boss(self):
        self.game_player.kill_boss()

    def upgrade(self):
        self.game_player.kill_boss()

    def get_proxy(self):
        return self

