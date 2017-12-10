from strategies.app2.base import App2


class Imp1(App2):
    __strategy_name__ = 'imp1'

    def m2(self):
        print "imp1"
