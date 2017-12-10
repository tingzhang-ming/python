from strategies.strategy import Strategy


class App1(Strategy):

    __strategy_ns__ = 'strategies.app1'
    __strategy_type__ = 'store'

    def m1(self):
        print "app1"

    def m2(self):
        pass
