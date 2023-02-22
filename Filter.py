students_multi = [("Christian", "A", 99), 
            ("Amun", "C", 80),
            ("Michael", "B", 60)]

age = lambda data: data[2]>=70

def age_function (data):
    return data[2]>=70

age_function_variable = age_function

pass_list = list(filter(age_function_variable,students_multi))

for i in pass_list:
    print(i)

