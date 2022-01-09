from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Frames')
root.iconbitmap('quakechamps.ico')

frame = LabelFrame(root, text="This is the created Frame...", padx=50, pady=50) # padding inside of the frame
frame.pack(padx=10, pady=10) # padding outside of the frame

button1 = Button(frame, text="don't click here", command=root.quit)
button2 = Button(frame, text="don't click here", command=root.quit)
button1.grid(row=0, column=0) # grid can be used inside a frame
button2.grid(row=0, column=1)

root.mainloop()
