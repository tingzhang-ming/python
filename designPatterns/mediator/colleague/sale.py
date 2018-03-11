from random import randint
from colleague import Colleague
from util import ACTIONS


class Sale(Colleague):

    def __init__(self, mediator):
        super(Sale, self).__init__(mediator)

    def sell_IBM_computer(self, number):
        self._mediator.execute(ACTIONS.sell_computer, number)
        print "sell IBM computer:", number

    def get_sale_status(self):
        sale_status = randint(0, 100)
        print "sell status: ", sale_status
        return sale_status

    def off_sale(self):
        self._mediator.execute(ACTIONS.off_sell)

