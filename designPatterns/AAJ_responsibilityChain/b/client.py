from handler import LEVELS
from handler.handlers import Father, Husband, Son
from women.women_c import Women
from processor import Processor


def main():
    f = Father()
    h = Husband()
    s = Son()
    processor = Processor([f, h, s])

    w1 = Women(LEVELS.father, "playing")
    processor.process(w1)

    w1 = Women(LEVELS.husband, "shopping")
    processor.process(w1)

    w1 = Women(LEVELS.son, "shangfen")
    processor.process(w1)


"""
daughter request father
daughter's request is playing
father response: agree
wife request husband
wife's request is shopping
husband response: agree
mother request son
mother's request is shangfen
son response: agree
"""


if __name__ == '__main__':
    main()
