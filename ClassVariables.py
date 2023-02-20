from OOP import Car

car_1 = Car("Mazda","Sedan",2006,"Silver")

car_2 = Car("Ford","Motorcycle",2020,"Red")

car_2.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)

Car.wheels = 2

print(Car.wheels)