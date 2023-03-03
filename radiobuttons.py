from tkinter import *

food = ["Ramen", "Udon", "Yakisoba"]

def order ():
    if(x.get()==0):
        print("You Ordered Ramne")
    elif(x.get()==1):
        print("You Ordered Udon")
    elif(x.get()==2):
        print("You Ordered Yakisoba")

window = Tk()

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[i],
                              variable=x,
                              value=i,
                              padx = 25,
                              font=("Arial", 20),
                              command=order)
    radiobutton.pack(anchor='w')


window.mainloop()