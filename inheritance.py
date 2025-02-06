# inherit attributes and methods from another class

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog("Rocky")
cat = Cat("Kity")
dog.eat()
dog.sleep()
cat.eat()
cat.sleep()


# multiple inheritance c(A, B)

class Predator():
    pass

class Prey():
    pass

class fish(Predator, Prey):
    pass


# multi level inheritance c(B)<-B(A)<-A

class Predator():
    pass

class Prey(Predator):
    pass

class fish(Prey):
    pass



























