

class Person:

    def __init__(self, name, age, genter):
        self.age = age
        self.genter = genter
        self.name = name

    def __str__(self):
        print self.name
        return self.name


def get_persons():
    res = []
    res.append(Person("aa", 11, "male"))
    res.append(Person("bb", 1, "male"))
    res.append(Person("cc", 2, "fmale"))
    res.append(Person("dd", 5, "fmale"))
    return res


def process_persons(roster, test, consume):
    for p in roster:
        if test(p):
            consume(p)


def print_name_consumer(p):
    print p.name


def t1():
    process_persons(get_persons(), lambda it: it.age > 4, print_name_consumer)


if __name__ == '__main__':
    t1()

