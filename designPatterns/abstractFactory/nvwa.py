from factory.HumanFactory import FemaleFactory, MaleFactory


def main():
    ff = FemaleFactory()
    mf = MaleFactory()
    fbh = ff.create_human("Black")
    mbh = mf.create_human("Black")
    for i in [fbh, mbh]:
        i.get_color()
        i.talk()
        i.get_sex()

if __name__ == '__main__':
    main()
