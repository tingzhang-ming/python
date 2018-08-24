from abc import ABCMeta, abstractmethod


class CarModel(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._sequence = []

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def alarm(self): pass

    def run(self):
        for action in self._sequence:
            if action == "start":
                self.start()
            elif action == "stop":
                self.stop()
            elif action == "alarm":
                self.alarm()
            else:
                raise Exception("Invalid action")

    def set_sequence(self, sequence):
        self._sequence = sequence

