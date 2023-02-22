import functools

letters = ["H","I", "L", "L"]
numbers = [1, 4, 6, 3 ,26, 64234]

words = functools.reduce(lambda x,y:x+y,letters)
sum = functools.reduce(lambda x,y:x+y,numbers)
print(words)
print(sum)