from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Sliders')
root.iconbitmap('quakechamps.ico')
root.geometry("400x400")

def show():
    label = Label(root, text=var.get())
    label.pack()

var = StringVar()

c = Checkbutton(root, text="Check box", variable=var, onvalue="True", offvalue="False")
c.deselect()
c.pack()

button = Button(root, text="Update value", command=show)
button.pack()

root.mainloop()
