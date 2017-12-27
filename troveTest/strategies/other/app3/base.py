from strategies.strategy import Strategy


class App3(Strategy):

    __strategy_ns__ = 'other.app3'
    __strategy_type__ = 'app'

    def m1(self):
        print "app3"

    def m2(self):
        pass
