from tkinter import *

def create_window():
    new_window = Tk()

    old_window.destroy()

def top_window():
    new_window = Toplevel()

old_window= Tk()

Button(old_window, text="Create New Window",command=create_window).pack()
Button(old_window, text="Create an Additional Window",command=top_window).pack()


old_window.mainloop()