#Use the same method with the same parameters in the child class to overwrite

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    
    def eat(self):
        print("The rabbit is eating")

rabbit = Rabbit()

rabbit.eat()