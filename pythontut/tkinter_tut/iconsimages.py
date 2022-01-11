# Import packages from modules
from tkinter import *
from PIL import ImageTk, Image

# Start of the main loop
root = Tk()

# Title of the main window
root.title('Icons, Images and Exit buttons')
#root.iconbitmap('quakechamps.ico')

# Open an image, place it in a label and show it on the screen
myimage = ImageTk.PhotoImage(Image.open("interceptor650.png"))
mylabel = Label(image=myimage)
mylabel.pack()

# Button for closing the main window
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# End of the main loop
root.mainloop()
