from other.app3.base import App3


class Imp1(App3):
    __strategy_name__ = 'imp1'

    def m2(self):
        print "imp1"
