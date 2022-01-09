from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap('ico/netfol.ico')

canvas = Canvas(root, height=300, width=600)
canvas.grid(columnspan=3, rowspan=3)

image = ImageTk.PhotoImage(Image.open("OIP.jfif"))
canvas.create_image(20, 20, anchor=NW, image=image)

label = Label(root, text="row=0 col=0")
label.grid(column=0, row=0)
label = Label(root, text="row=0 col=1")
label.grid(column=1, row=0)
label = Label(root, text="row=0 col=2")
label.grid(column=2, row=0)

label = Label(root, text="row=1 col=0")
label.grid(column=0, row=1)
label = Label(root, text="row=1 col=1")
label.grid(column=1, row=1)
label = Label(root, text="row=1 col=2")
label.grid(column=2, row=1)

button = Button(root, text="Close window", command=root.quit)
button.grid(column=2, row=2)

root.mainloop()
