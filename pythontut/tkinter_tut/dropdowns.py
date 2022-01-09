from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Dropdown Menus')
root.iconbitmap('quakechamps.ico')
root.geometry("400x400")

# Dropdown boxes
def show():
    label = Label(root, text=var.get())
    label.pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

var = StringVar()
var.set("Choose a day")

drop = OptionMenu(root, var, *options)
drop.pack()

button = Button(root, text="Show selected", command=show)
button.pack()

root.mainloop()
