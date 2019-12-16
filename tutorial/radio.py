from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('frame - tutorial')
root.iconbitmap('images/diablo.ico')

#r = IntVar()


# text , mode
MODES = [
    ('Pepperoni','Pepperoni'),
    ('Cheese','Cheese'),
    ('Mushrooms','Mushrooms'),
    ('Onion','Onion'),
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W, padx=50, pady=5)


def optionClick(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text='Option 1', variable=r, value=1, command = lambda : optionClick(r.get())).pack()
#Radiobutton(root, text='Option 2', variable=r, value=2, command = lambda : optionClick(r.get())).pack()

myButton = Button(root, text='Click Me!', command = lambda: optionClick(pizza.get())).pack(padx=50, pady=10)

root.mainloop()