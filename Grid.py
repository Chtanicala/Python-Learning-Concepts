from tkinter import *

def submit():
    firstName = firstNameEntry.get()
    lastName = lastNameEntry.get()
    email = emailNameEntry.get()

    print("First Name:",firstName,"Last Name:",lastName,"Email:",email)

window = Tk()

titleLabel = Label(window,text="Enter your info", font=("Arial", 25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window, text="First Name: ", width=20,bg="red").grid(column=0,row=1)
firstNameEntry = Entry(window)
firstNameEntry.grid(column=1,row=1)

lastNameLabel = Label(window, text="Last Name: ",bg="yellow").grid(column=0,row=2)
lastNameEntry = Entry(window)
lastNameEntry.grid(column=1,row=2)

emailNameLabel = Label(window, text="Email: ",bg="green").grid(column=0,row=3)
emailNameEntry = Entry(window)
emailNameEntry.grid(column=1,row=3)

submitButton = Button(window, text="Submit", command=submit).grid(row=4,column=0,columnspan=2)

window.mainloop()