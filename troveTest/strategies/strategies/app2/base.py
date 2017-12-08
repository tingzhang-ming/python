from strategies.strategy import Strategy


class App2(Strategy):

    __strategy_ns__ = 'app2'
    __strategy_type__ = 'manage'

    def m1(self):
        print "app2"

    def m2(self):
        pass
