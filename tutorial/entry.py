from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth = 5)
e.pack()
e.insert(0, 'Name') # 0 is for index 0, only one entry therefore 0?
e.get()

def myClick():
    msg = 'Saved your name \'' + e.get() + '\''
    myLabel = Label(root, text=msg)
    myLabel.pack()

myButton = Button(root, text='Enter Your Name!',command=myClick) # OBS! no function paranthesis
myButton.pack()

root.mainloop()