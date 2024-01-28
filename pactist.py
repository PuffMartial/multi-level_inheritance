class Organisim:
    alive = True

class Animal(Organisim):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("thi dog is barking")


dog = Dog()
dog.eat()
dog.bark