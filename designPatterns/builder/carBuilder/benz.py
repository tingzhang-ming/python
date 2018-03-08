from carBuilder import CarBuilder
from car.benz import BenzModel


class BenzBuilder(CarBuilder):

    def __init__(self):
        super(BenzBuilder, self).__init__()
        self._benz = BenzModel()

    def get_car_model(self):
        return self._benz

    def set_sequence(self, sequence):
        self._benz.set_sequence(sequence)
