from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('images - tutorial')

# Does not work fore some unclear reason
root.iconbitmap('images/diablo.ico')

img_1 = ImageTk.PhotoImage(Image.open('images/test.png'))
img_2 = ImageTk.PhotoImage(Image.open('images/fireMario_PF.png'))
img_3 = ImageTk.PhotoImage(Image.open('images/filter.png'))

img_list = [img_1, img_2, img_3]
img_nmr = 0
img_label = Label(image=img_1)
img_label.grid(row=0, column=0,columnspan=3)


def forward():
    global img_nmr, img_label
    if img_nmr != len(img_list)-1:
        img_nmr += 1
    img_label.grid_forget()
    img_label = Label(image=img_list[img_nmr])
    img_label.grid(row=0, column=0,columnspan=3)  


def backward():
    global img_nmr, img_label
    if img_nmr != 0:
        img_nmr -= 1
    img_label.grid_forget()
    img_label = Label(image=img_list[img_nmr])
    img_label.grid(row=0, column=0,columnspan=3)  


button_back = Button(root, text = '<<', command = lambda: backward())
button_exit = Button(root, text = 'EXIT PROGRAM', command=root.quit)
button_forw = Button(root, text = '>>', command = lambda: forward())

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forw.grid(row=1,column=2)



root.mainloop()