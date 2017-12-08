from other.app3.base import App3


class Imp2(App3):
    __strategy_name__ = 'imp2'

    def m2(self):
        print "imp2"
