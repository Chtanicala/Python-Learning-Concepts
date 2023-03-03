from tkinter import *

def display():
    if(x.get()==1):
        print("You Agree")
    else:
        print("You Don't Agree")


window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text = "Agree to Terms and Conditions",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial",20),
                           fg="red",
                           background="black",
                           activebackground="red",
                           activeforeground="black",
                           padx=25,
                           pady=25)

check_button.pack()

window.mainloop()