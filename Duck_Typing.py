class Duck:
    def walk(self):
        print("The duck is walking")
    def talk(self):
        print("the duck is quacking")

class Chicken:
    def walk(self):
        print("The chicken is walking")
    def talk(self):
        print("the chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

person.catch(chicken)