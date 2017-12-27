

def create_animal_class():
    """
    Return an Animal class, built by invoking the type constructor.
    """
    def init(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass

    return type('Animal2', (object,), {
        '__doc__': 'a class of animal',
        '__init__': init,
        'eat': eat,
        'go_to_vet': go_to_vet,
    })


def create_animal_class2():
    """
    Return an Animal class, built by invoking the type constructor.
    """

    class Animal(object):
        def __init__(self, name):
            self.name = name

        def eat(self):
            pass

        def go_to_vet(self):
            pass
    return Animal
