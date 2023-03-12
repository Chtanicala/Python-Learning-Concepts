from tkinter import *

def doSomething(event):
    print("You did something " + str(event.x) + " , " + str(event.y))

window = Tk()

#Left Mouse Click
window.bind("<Button-1>", doSomething)
#Middle Mouse Click
window.bind("<Button-2>", doSomething)
#Right Mouse Click
window.bind("<Button-3>", doSomething)
#Button Release
window.bind("<ButtonRelease>",doSomething)
#Enter the Window
window.bind("<Enter>",doSomething)
#Leave the Window
window.bind("<Leave>",doSomething)
#Where the Mouse Moves
window.bind("<Motion>",doSomething)

window.mainloop()