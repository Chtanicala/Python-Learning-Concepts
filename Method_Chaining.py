class Car:
    def turn_on(self):
        print("Engine Start")
        return self
    def drive(self):
        print("Car Drive")
        return self

    def brake(self):
        print("Car Stop")
        return self
    def turn_off(self):
        print("Engine Off")
        return self

car = Car()

car.turn_on().drive().brake().turn_off()