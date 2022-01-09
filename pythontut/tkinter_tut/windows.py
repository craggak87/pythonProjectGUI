from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

root.title('Windows!')
root.iconbitmap('quakechamps.ico')

def open():
    global image
    top = Toplevel(root)
    top.title('Windows!Top')
    top.iconbitmap('quakechamps.ico')
    label = Label(top, text="Text in top window!").pack()
    image = ImageTk.PhotoImage(Image.open("interceptor650.png"))
    img_label = Label(top, image=image).pack()
    button2 = Button(top, text="Close window", command=top.destroy).pack()

button = Button(root, text="Open top window", command=open).pack()


root.mainloop()
