from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Sliders')
root.iconbitmap('quakechamps.ico')
root.geometry("400x400")

vertical = Scale(root, from_=200, to=600)
vertical.pack()

horizontal = Scale(root, from_=200, to=600, orient=HORIZONTAL)
horizontal.pack()

def slide():
    horiz_label = Label(root, text=horizontal.get())
    horiz_label.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

button = Button(root, text="update slide value", command=slide)
button.pack()

root.mainloop()
