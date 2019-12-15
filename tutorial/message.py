from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('frame - tutorial')
root.iconbitmap('images/dibalo.ico')


def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askyesno('This is my popup!','Hello World!')
    #Label(root, text=response).pack() #yes==1, no==0
    if response == 1:
        Label(root, text='You clicked yes.').pack()
    elif response == 0:
        Label(root, text='You clicked no.').pack()
    

Button(root, text='Popup', command=popup).pack()


root.mainloop()