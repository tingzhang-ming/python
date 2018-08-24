from carBuilder import CarBuilder
from car.bmw import BMWModel


class BMWBuilder(CarBuilder):

    def __init__(self):
        super(BMWBuilder, self).__init__()
        self._bmw = BMWModel()

    def get_car_model(self):
        return self._bmw

    def set_sequence(self, sequence):
        self._bmw.set_sequence(sequence)
