from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Select file')
root.iconbitmap('images/dibalo.ico')
root.geometry("200x200")

def show():
    lbl = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text='check this box!', variable=var, onvalue='on', offvalue='off')
c.deselect()
c.pack()


btn = Button(root, text='See what is checked.', command = show).pack()




Button(root, text='Exit', command=root.quit).pack()
root.mainloop()


