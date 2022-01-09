from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Image Viewer')
root.iconbitmap('quakechamps.ico')

myimage1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
myimage2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
myimage3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
myimage4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
myimage5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

image_list = [myimage1, myimage2, myimage3, myimage4, myimage5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

mylabel = Label(image=myimage1)
mylabel.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global mylabel
	global button_fwd
	global button_back

	mylabel.grid_forget()
	mylabel = Label(image=image_list[image_number-1])

	button_fwd = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 5:
		button_fwd = Button(root, text=">>", state=DISABLED)

	mylabel.grid(row=0, column=0, columnspan=3)

	button_back.grid(row=1, column=0)
	button_fwd.grid(row=1, column=2)

	status = Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
	global mylabel
	global button_fwd
	global button_back

	mylabel.grid_forget()
	mylabel = Label(image=image_list[image_number-1])

	button_fwd = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	mylabel.grid(row=0, column=0, columnspan=3)

	button_back.grid(row=1, column=0)
	button_fwd.grid(row=1, column=0)

	status = Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_back.grid(row=1, column=0)

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.grid(row=1, column=1)

button_fwd = Button(root, text=">>", command=lambda: forward(2))
button_fwd.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
