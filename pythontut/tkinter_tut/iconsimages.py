from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Icons, Images and Exit buttons')
#root.iconbitmap('/home/craggak/pythontut/tkinter_tut/quakechamps.ico')

myimage = ImageTk.PhotoImage(Image.open("interceptor650.png"))
mylabel = Label(image=myimage)
mylabel.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
