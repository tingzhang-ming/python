

class Colleague(object):

    def __init__(self, mediator):
        self._mediator = mediator
        self._mediator.bind(self)
