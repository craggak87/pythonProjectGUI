from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

root.title('File dialog')
root.iconbitmap('quakechamps.ico')

def open():
    global image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/alexh/Desktop/pythontut/tkintertut/images", title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    label = Label(root, text=root.filename).pack()

    image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(image=image).pack()

button = Button(root, text="Open file", command=open).pack()

root.mainloop()
