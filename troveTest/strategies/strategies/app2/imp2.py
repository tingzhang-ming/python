from strategies.app2.base import App2


class Imp2(App2):
    __strategy_name__ = 'imp2'

    def m2(self):
        print "imp2"
