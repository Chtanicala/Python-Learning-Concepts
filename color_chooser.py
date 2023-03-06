from tkinter import *
from tkinter import colorchooser


#Customize Character 
def color():
    color_var = colorchooser.askcolor()

    window.config(bg=color_var[1])
window = Tk()

window.geometry("420x420")

button = Button(window, text="Choose a Color", command=color)
button.pack()


window.mainloop()