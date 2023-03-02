from tkinter import *

window = Tk()

click_count = 0

def click():
    global click_count
    click_count += 1
    print("You clicked the button:", click_count, "times")

button = Button(window,
                text="Click Me!",
                command=click,
                font=("Comic Sans", 40),
                fg="Red",
                bg="black",
                activebackground="red",
                activeforeground="black",
                state=ACTIVE)

button.pack()

window.mainloop()