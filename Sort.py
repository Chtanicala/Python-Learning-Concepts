students = ["Christian", "Amun", "Michael", "Angela"]
students_tuple = ("Christian", "Amun", "Michael", "Angela")
students_multi = [("Christian", "A", 99), 
            ("Amun", "C", 80),
            ("Michael", "B", 90)]
students_multi_tuple = (("Christian", "A", 99), 
            ("Amun", "C", 80),
            ("Michael", "B", 90))

grade = lambda grades:grades[1]

sorted_students = sorted(students_tuple)
sorted_tuple = sorted(students_multi_tuple,key=grade)
students.sort(reverse=True)

for i in students:
    print(i)

for i in sorted_students:
    print(i)


students_multi.sort(key=grade)

for i in students_multi:
    print(i)

for i in sorted_tuple:
    print(i)