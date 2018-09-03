

class Context(object):

    def __init__(self, strategy):
        self._strategy = strategy

    def operate(self):
        self._strategy.operate()
