import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(2)
    print("You studied")

x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=())
x.start()
y.start()
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())