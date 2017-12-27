from strategies.app1.base import App1


class Imp1(App1):
    __strategy_name__ = 'imp1'

    def __init__(self):
        super(Imp1, self).__init__()

    def m2(self):
        print "imp1"
