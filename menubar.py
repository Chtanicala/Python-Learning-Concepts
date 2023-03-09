from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("File Cut")

def copy():
    print("File Copied")

def paste():
    print("File Paste")


window = Tk()


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0,font=("Comic Sans",10))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0,font=("Comic Sans",10))
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()