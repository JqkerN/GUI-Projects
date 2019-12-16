from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Dropdown Meny')
root.iconbitmap('images/diablo.ico')
root.geometry("200x200")


def show():
    lbl = Label(root, text=clicked.get()).pack()

options = [
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thursday', 
    'Friday',
    'Saturday',
    ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text='Show Selection', command=show)
btn.pack()

Button(root, text='Exit', command=root.quit).pack()
root.mainloop()


