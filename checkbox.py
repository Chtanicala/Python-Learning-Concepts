from tkinter import *


def submit():
    username = entry.get()
    print(username)

def delete():
    entry.delete(0,END)

def backspace():
    length = len(entry.get())
    start = length-1

    entry.delete(start,END)

window = Tk()

entry = Entry(window,
              font=("Arial",50))

entry.pack(side = LEFT)

submit_button = Button(window, text ="submit", command = submit)
submit_button.pack(side = RIGHT)


delete_button = Button(window, text ="delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text ="backspace", command = backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()