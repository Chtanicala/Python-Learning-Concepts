usernames = ["Christian", "Amun", "Michael"]
passwords = ("password", "abc123", "guest")
login_dates = ["1/2/23", "1/23/23", "1/4/22"]

users = zip(usernames, passwords, login_dates)

for i in users:
    print(i)