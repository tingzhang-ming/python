from actor import OldActor
from role import KungFuRole


def main():
    actor = OldActor()
    role = KungFuRole()
    role.accept(actor)


if __name__ == '__main__':
    main()
