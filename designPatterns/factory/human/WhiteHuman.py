from human import Human

class WhiteHuman(Human):

    def get_color(self):
        print "white human's skin is white."

    def talk(self):
        print "white human talk..."


class MaleWhiteHuman(WhiteHuman):
    def get_sex(self):
        print "White male...."


class FemaleWhiteHuman(WhiteHuman):
    def get_sex(self):
        print "White female...."