from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\paint\\OneDrive\\Documents\\Coding",
                                           title="Open a File",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open",command=openFile)

button.pack()

window.mainloop()