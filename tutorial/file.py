from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Select file')
root.iconbitmap('images/diablo.ico')

img = []

def openPicture():
    global img
    dir = "images/"
    root.filename = filedialog.askopenfilename(initialdir=dir,
                                                title='Select A File', 
                                                filetypes=(('png file','*.png'),('all files',"*.*"))) 
    lbl = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=img).pack()

btn = Button(root, text='Open File', command=openPicture).pack()

root.mainloop()

