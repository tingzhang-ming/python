from abc import ABCMeta, abstractmethod


class HummerModel(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def alarm(self): pass

    def run(self):
        self.start()
        self.alarm()
        self.stop()

