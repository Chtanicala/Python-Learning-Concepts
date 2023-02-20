class Car:
    
    wheels = 4 #class variable

    #constructor, assigning attributes
    def __init__(self,make,model,year,color):
        self.make = make #instance variables
        self.model = model #instance variables
        self.year = year #instance variables
        self.color = color #instance variables

    def drive(self):
        print("This " + self.make + " is driving")

    def stop (self):
        print("This " + self.make + " is stopped")


