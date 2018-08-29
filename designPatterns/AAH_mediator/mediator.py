from abc import ABCMeta, abstractmethod
from colleague.purchase import Purchase
from colleague.stock import Stock
from colleague.sale import Sale


class AbstractMediator(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._purchase = None
        self._sale = None
        self._stock = None

    def bind(self, *obs):
        for ob in obs:
            print type(ob)
            if type(ob) is Purchase:
                self._purchase = ob
            elif type(ob) is Stock:
                self._stock = ob
            elif type(ob) is Sale:
                self._sale = ob
            else:
                print 'unknow type: ', type(ob)

    @abstractmethod
    def execute(self, action, *args): pass


class Mediator(AbstractMediator):

    def execute(self, action, *args):
        largs = [str(a) for a in args]
        cmd = 'self._{}({})'.format(action, ','.join(largs))
        eval(cmd)

    def _buy_computer(self, number):
        sale_status = self._sale.get_sale_status()
        if sale_status > 80:
            print "buy IBM computer number: ", number
            self._stock.increase(number)
        else:
            buy_number = number / 2
            print "buy IBM computer number: ", buy_number

    def _sell_computer(self, number):
        if self._stock.get_stock_number() < number:
            self._purchase.buy_IBM_computor(number)
        self._stock.decrease(number)

    def _off_sell(self):
        print "off selle computer number: ", self._stock.get_stock_number()

    def _clear_stock(self):
        self._sale.off_sale()
        self._purchase.refuse_buy_IBM()


