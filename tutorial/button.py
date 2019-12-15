from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='You did click.')
    myLabel.pack()

myButton = Button(root, text='Click Here!',
                padx=50,pady=20,command=myClick, 
                fg='red', bg='black')
myButton.pack()

root.mainloop()