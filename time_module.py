import time

print(time.ctime(0)) #seconds since epoch and make it readable date and time

print(time.time()) #current seconds since epoch

print(time.ctime(time.time())) #current date and time

time_object = time.localtime()

print(time_object)

local_time = time.strftime("%B %D %H:%M:%S",time_object)
print(local_time)

time_string = "19 April, 2019"
time_object = time.strptime(time_string, "%d %B, %Y")

print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 3, 0, 0, 0)
time_string = time.asctime(time_tuple)

print(time_string)

time_tuple = (2020, 4, 20, 4, 20, 3, 0, 0, 0)
time_string = time.mktime(time_tuple)

print(time_string)