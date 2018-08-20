import emperor as er


def main():
    emperor = er.get_instance()
    emperor.name = "haha"
    for i in range(3):
        emperor = er.get_instance()
        emperor.say()

if __name__ == '__main__':
    e = er.Emperor()
    main()
