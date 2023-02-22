students = [("Christian", "A", 50), 
            ("Amun", "C", 45),
            ("Michael", "B", 40)]

to_percent = lambda score: (score[0],score[1],score[2]/50*100)

def percent_conversion(score):
    return (score[0],score[1],score[2]/50*100)

to_percent = percent_conversion

store_percents = map(to_percent,students)

for i in store_percents:
    print(i)