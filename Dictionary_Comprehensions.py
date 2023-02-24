boys_grades = {"Christian": 50, 
                    "Amun": 45,
                    "Michael": 40}

grades_in_percent = {key: (value/50*100) for (key,value) in boys_grades.items()}

print(grades_in_percent)

grades_in_percent = {key: (value/50*100) for (key,value) in boys_grades.items() if value > 40}

print(grades_in_percent)

grades_in_percent = {key: ((value/50*100) if value > 40 else "Failed") for (key,value) in boys_grades.items()}

print(grades_in_percent)