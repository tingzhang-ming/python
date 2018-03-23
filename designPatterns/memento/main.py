

class Memento(object):

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state


class Caretaker(object):

    def __init__(self):
        self._memento = None

    def get_memento(self):
        return self._memento

    def set_memento(self, memento):
        self._memento = memento


class Boy(object):

    def __init__(self):
        self._state = ""

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self.set_state(memento.get_state())


def main():
    b = Boy()
    c = Caretaker()
    b.set_state("good")
    print b.get_state()
    c.set_memento(b.create_memento())
    b.set_state("bad")
    print b.get_state()
    b.restore_memento(c.get_memento())
    print b.get_state()


if __name__ == '__main__':
    main()

# good
# bad
# good
