from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="Hacked",
                        #message="You've been hacked")
    
    #messagebox.showwarning(title="Hacked",
                            #message="You've been hacked")

    #messagebox.showerror(title="Hacked",
                            #message="You've been hacked")
    #if messagebox.askokcancel(title="Ask Ok Cancel", message="Nuke Mars?") == True:
        #print("Mars is Gone")
    #else:
        #print("Crisis averted")     
    
    #if messagebox.askretrycancel(title="Ask Ok Cancel", message="Nuke Mars?") == True:
        #print("Mars is Gone")
    #else:
        #print("Crisis averted")  
    
    #if messagebox.askyesno(title="Ask Ok Cancel", message="Nuke Mars?") == True:
        #print("Mars is Gone")
    #else:
        #print("Crisis averted")
    
    #answer = messagebox.askquestion(title="Ask Ok Cancel", message="Nuke Mars?")

    #if answer == 'yes':
        #messagebox.showinfo(title="Mars Is Gone",
                            #message="What have you done?")
    #else:
        #messagebox.showinfo(title="Crisis Averted",
                            #message="Congrats!")

    answer = messagebox.askyesnocancel(title="Life", message="End Life On Earth?", icon='warning')
    if answer == True:
        print("Good Bye Earth")
    elif answer == False:
        print("Coward")
    else:
        print("Super Coward")
        
window = Tk()

button = Button(window,
                command=click,
                text="Click Me")

button.pack()

window.mainloop()