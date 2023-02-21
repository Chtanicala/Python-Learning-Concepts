class Car:
    color = None

class Motorcycle:
    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
bike_1 = Motorcycle()
car_2 = Car()

change_color(car_1, "red")
change_color(bike_1, "blue")
change_color(car_2, "yellow")

print(car_1.color)
print(bike_1.color)
print(car_2.color)
