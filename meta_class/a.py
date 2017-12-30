
class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass


class Cat(Animal):

    def meow(self):
        pass

    def purr(self):
        pass

# -----------------------------


def init(self, name):
    self.name = name


def eat(self):
    pass


def go_to_vet(self):
    pass

Animal2 = type('Animal2', (object,), {
    '__doc__': 'a class of animal',
    '__init__': init,
    'eat': eat,
    'go_to_vet': go_to_vet,
})


def t1():
    a = Animal2('mhc')
    for i in vars(a).keys():
        print i
    print a.name
    print dir(a)

# -----------------------------------------


def meow(self):
    return None


def purr(self):
    return None


Cat2 = type('Cat', (Animal2,), {
    'meow': meow,
    'purr': purr,
})


if __name__ == '__main__':
    t1()
