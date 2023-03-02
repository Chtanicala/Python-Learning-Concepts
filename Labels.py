from tkinter import *

window = Tk()

label = Label(window,
              text="Hello World",
              font=('Comic Sans', 69, "bold"),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=photo)

label.pack()

window.mainloop()