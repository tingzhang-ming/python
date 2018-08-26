from colleague import Colleague
from util import ACTIONS


class Purchase(Colleague):

    def __init__(self, mediator):
        super(Purchase, self).__init__(mediator)

    def buy_IBM_computor(self, number):
        self._mediator.execute(ACTIONS.buy_computer, number)

    def refuse_buy_IBM(self):
        print "not buy IBM"
