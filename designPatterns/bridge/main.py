from abc import ABCMeta, abstractmethod


class Product(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def be_producted(self):
        pass

    @abstractmethod
    def be_selled(self):
        pass


class House(Product):

    def be_producted(self):
        print "product house"

    def be_selled(self):
        print "sell house"


class IPod(Product):

    def be_producted(self):
        print "product ipod"

    def be_selled(self):
        print "sell ipod"


class AbstractCorp(object):

    __metaclass__ = ABCMeta

    def __init__(self, product):
        self._product = product

    def make_money(self):
        self._product.be_producted()
        self._product.be_selled()


class HouseCorp(AbstractCorp):

    def __init__(self, house):
        super(HouseCorp, self).__init__(house)

    def make_money(self):
        super(HouseCorp, self).make_money()
        print "house corp make big money..."


class ShanZhaiCorp(AbstractCorp):

    def __init__(self, product):
        super(ShanZhaiCorp, self).__init__(product)

    def make_money(self):
        super(ShanZhaiCorp, self).make_money()
        print "I make money..."


def main():
    house = House()
    house_corp = HouseCorp(house)
    house_corp.make_money()

    shanzhai = ShanZhaiCorp(IPod())
    shanzhai.make_money()


if __name__ == '__main__':
    main()
