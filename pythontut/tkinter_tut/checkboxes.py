# Import packages from modules
from tkinter import *
from PIL import ImageTk, Image

# Start of the main loop
root = Tk()

# Title, icon and sizing of the main window
root.title('Sliders')
root.iconbitmap('quakechamps.ico')
root.geometry("400x400")

# Function for showing the updated value
def show():
    label = Label(root, text=var.get())
    label.pack()

var = StringVar()

# Checkbox syntax
c = Checkbutton(root, text="Check box", variable=var, onvalue="True", offvalue="False")
c.deselect()
c.pack()

# Button to show the value of the checkbox
button = Button(root, text="Update value", command=show)
button.pack()

# End of the main loop
root.mainloop()
