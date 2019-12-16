from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('frame - tutorial')
root.iconbitmap('images/diablo.ico')

frame = LabelFrame(root, text='This is my Frame...', padx=50, pady=50)
frame.pack(padx=10, pady=10)

button_1 = Button(frame, text='EXIT',command=root.quit)
button_2 = Button(frame, text='You can exit here 2 ',command=root.quit)

button_1.grid(row=0,column=0) # can use grid inside of a frame!!!
button_2.grid(row=1,column=1) # can use grid inside of a frame!!!


root.mainloop()