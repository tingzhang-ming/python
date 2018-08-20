from human import Human


class YellowHuman(Human):

    def get_color(self):
        print "yellow human's skin is yellow."

    def talk(self):
        print "yellow human talk..."


class MaleYellowHuman(YellowHuman):
    def get_sex(self):
        print "Yellow male...."


class FemaleYellowHuman(YellowHuman):
    def get_sex(self):
        print "Yellow female...."