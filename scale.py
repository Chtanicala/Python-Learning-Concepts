from tkinter import *

def submit():
    print("The Tempature is", scale.get(), "degrees C")

window = Tk()

scale = Scale(window,from_=100,to=0,
              length=500,
              orient=VERTICAL,
              font=("Arial",20),
              tickinterval = 10,
              bg ="#69EAFF",
              fg = "black",
              troughcolor="white")

scale.set(((scale['from']-scale['to'])/2+scale['to']))
scale.pack()

button = Button(window,text="submit",
                command=submit)
button.pack()

window.mainloop()