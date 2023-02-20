class Car:
    
    #constructor, assigning attributes
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.make + " is driving")

    def stop (self):
        print("This " + self.make + " is stopped")

car_1 = Car("Mazda","Sedan",2006,"Silver")

car_1.drive()
car_1.stop()