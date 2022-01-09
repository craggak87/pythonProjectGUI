from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Radio buttons')
root.iconbitmap('quakechamps.ico')

frame = LabelFrame(root, text="This is the created Frame...", padx=50, pady=50) # padding inside of the frame
frame.pack(padx=10, pady=10) # padding outside of the frame

button1 = Button(frame, text="don't click here", command=root.quit)
button2 = Button(frame, text="don't click here", command=root.quit)
button1.grid(row=0, column=0) # grid can be used inside a frame
button2.grid(row=0, column=1)

#r = IntVar()
#r.set("2") # automatically selects the option

toppings = [
    ("Greek", "Greek"),
    ("Vegaroma", "Vegaroma"),
    ("Chicken", "Chicken"),
    ("Tuna", "Tuna"),
]
pizza = StringVar()
pizza.set("Greek")

for text, mode in toppings:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    label = Label(root, text=value)
    label.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 4", variable=r, value=4, command=lambda: clicked(r.get())).pack()

#label = Label(root, text=r.get())
#label.pack()

button3 = Button(root, text="don't click here", command=lambda: clicked(pizza.get()))
button3.pack()

root.mainloop()
