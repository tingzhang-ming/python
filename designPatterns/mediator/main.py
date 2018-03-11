from mediator import Mediator
from colleague.purchase import Purchase
from colleague.sale import Sale
from colleague.stock import Stock


def main():

    mediator = Mediator()

    p = Purchase(mediator)
    s = Sale(mediator)
    stock = Stock(mediator)

    p.buy_IBM_computor(100)
    s.sell_IBM_computer(1)
    stock.clear_stock()


if __name__ == '__main__':
    main()
