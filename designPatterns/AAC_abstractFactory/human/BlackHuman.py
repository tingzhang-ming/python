from abc import abstractmethod
from human import Human


class BlackHuman(Human):

    __metaclass__ = type(Human)

    def get_color(self):
        print "black human's skin is black."

    def talk(self):
        print "black human talk..."

    @abstractmethod
    def get_sex(self):
        pass


class MaleBlackHuman(BlackHuman):

    def get_sex(self):
        print "black male...."


class FemaleBlackHuman(BlackHuman):

    def get_sex(self):
        print "black female...."