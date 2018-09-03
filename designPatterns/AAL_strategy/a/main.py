from context import Context
from strategies import BackDoor, GivenGreenLight, BlockEnemy


def main():
    s = BackDoor()
    context = Context(s)
    context.operate()

    s = GivenGreenLight()
    context = Context(s)
    context.operate()

    s = BlockEnemy()
    context = Context(s)
    context.operate()


if __name__ == '__main__':
    main()
