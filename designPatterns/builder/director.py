from carBuilder.benz import BenzBuilder
from carBuilder.bmw import BMWBuilder


class Director(object):

    def __init__(self):
        self._sequence = []
        self._benz_builder = BenzBuilder()
        self._bmw_builder = BMWBuilder()

    def get_a_benz_model(self):
        del self._sequence[:]
        self._sequence.append("start")
        self._sequence.append('alarm')
        self._benz_builder.set_sequence(self._sequence)
        return self._benz_builder.get_car_model()

    def get_b_benz_model(self):
        del self._sequence[:]
        self._sequence.append('alarm')
        self._sequence.append("stop")
        self._benz_builder.set_sequence(self._sequence)
        return self._benz_builder.get_car_model()

    def get_a_bmw_model(self):
        del self._sequence[:]
        self._sequence.append("start")
        self._sequence.append('alarm')
        self._bmw_builder.set_sequence(self._sequence)
        return self._bmw_builder.get_car_model()

