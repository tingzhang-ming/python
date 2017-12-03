
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.name2 = "hahah"



class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def saySomething(self):
        print (self.name)
        print (self.name2)

if __name__ == '__main__':
    d = Dog("m")
    print d.saySomething()
