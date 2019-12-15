from tkinter import *

# Initializing root
root = Tk()

myLabel1 = Label(root, text='Write some text here!')
myLabel2 = Label(root, text='Something more...')
myLabel1.pack() # Can use grid(row=0, column=0) instead aswell.
myLabel2.pack()
root.mainloop()