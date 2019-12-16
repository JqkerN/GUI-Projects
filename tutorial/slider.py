from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Select file')
root.iconbitmap('images/diablo.ico')
root.geometry("200x200")

def slide():
    #lbl = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()) )


vertical = Scale(root, from_=200, to=400)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL)
horizontal.pack()



btn = Button(root, text='Click me!', command=slide).pack()
Button(root, text='Exit', command=root.quit).pack()
root.mainloop()

