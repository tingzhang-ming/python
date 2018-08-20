import emperor as er


def main():
    emperor = er.Emperor()
    emperor.name = "haha"
    emperor.say()
    for i in range(3):
        emperor = er.Emperor()
        emperor.say()

if __name__ == '__main__':
    main()

