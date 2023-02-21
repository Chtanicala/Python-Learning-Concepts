from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")


vehicle = Vehicle()

car = Car()

motorcycle = Motorcycle()

car.go()
motorcycle.go()