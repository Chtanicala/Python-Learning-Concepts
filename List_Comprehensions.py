squares = []
for i in range(1,11):
    squares.append(i*i)

print(squares)
#list comprehension
squares = [i*i for i in range(1,11)]
print(squares)

#list comprehension with lambda
students = [100,90,70,80,20,30,40,50,60]
passed_students = list(filter(lambda x :x>=60,students))

print(passed_students)
#without lambda
passed_students = [i if i >= 60 else "Failed" for i in students ]

print(passed_students)
