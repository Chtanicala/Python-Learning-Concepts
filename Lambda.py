double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z:x+y+z
full_name = lambda first_name, last_name: first_name + " " +last_name
age_check = lambda age:True if age >= 18 else False

print(double(2))
print(multiply(3,2))
print(add(3,2,5))

print(full_name("Christian","Tanicala"))
print(age_check(14))