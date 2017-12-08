from strategies.app1.base import App1


class Imp2(App1):
    __strategy_name__ = 'imp2'

    def __init__(self):
        super(Imp2, self).__init__()

    def m2(self):
        print "imp2"
