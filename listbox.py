from tkinter import*

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    print("You have ordered:")
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
    

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

x = IntVar()

listbox = Listbox(window,
                  background="red",
                  fg="white",
                  font=("Constantia",35),
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Breadsticks")
listbox.insert(3,"Cinnamon Twists")
listbox.insert(4,"Salad")
listbox.insert(5,"Wings")

listbox.config(height=listbox.size())
listbox.config(width=20)

entryBox = Entry(window,
                 width=20)
entryBox.pack()

submitButton = Button(window,
                      command=submit,
                      text="Order"
                      )
submitButton.pack()

addButton = Button(window,
                      command=add,
                      text="Add"
                      )
addButton.pack()

delButton = Button(window,
                      command=delete,
                      text="Delete"
                      )
delButton.pack()

window.mainloop()