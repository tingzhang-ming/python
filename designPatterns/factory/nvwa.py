from factory.HumanFactory import HumanFactory


def main():
    yin_yang_lu = HumanFactory()
    white_human = yin_yang_lu.create_human("WhiteHuman")
    white_human.get_color()
    white_human.talk()

    black_human = yin_yang_lu.create_human("BlackHuman")
    black_human.get_color()
    black_human.talk()

    yellow_human = yin_yang_lu.create_human("YellowHuman")
    yellow_human.get_color()
    yellow_human.talk()

if __name__ == '__main__':
    main()

# white human's skin is white.
# white human talk...
# black human's skin is black.
# black human talk...
# yellow human's skin is yellow.
# yellow human talk...
