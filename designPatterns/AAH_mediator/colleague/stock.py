from colleague import Colleague
from util import ACTIONS


class Stock(Colleague):

    COMPUTER_NUMBER = 100

    def __init__(self, mediator):
        super(Stock, self).__init__(mediator)

    def increase(self, number):
        # type(self).COMPUTER_NUMBER += number
        self.COMPUTER_NUMBER += number
        print "stock number is :", self.COMPUTER_NUMBER

    def decrease(self, number):
        # type(self).COMPUTER_NUMBER -= number
        self.COMPUTER_NUMBER -= number
        print "stock number is :", self.COMPUTER_NUMBER

    def get_stock_number(self):
        return self.COMPUTER_NUMBER

    def clear_stock(self):
        print "clear number is:", self.COMPUTER_NUMBER
        self._mediator.execute(ACTIONS.clear_stock)
