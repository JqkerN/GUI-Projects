from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('1th window')
root.iconbitmap('images/diablo.ico')


img = ImageTk.PhotoImage(Image.open('images/diablo.ico'))
# add window
def openWindow():
    global img
    top = Toplevel()
    top.title('2nd Window')
    top.iconbitmap('images/diablo.ico')
    Label(top, image=img).pack()
    Button(top, text='Close Window',command=top.destroy).pack()
    
Button(root, text='Open iconbitmap',command=openWindow).pack()
Button(root, text='EXIT',command=root.quit).pack()
        
root.mainloop()