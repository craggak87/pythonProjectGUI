from tkinter import *

#Start of the main loop

root = Tk()
root.title("Window title")
#When the button is pressed it will run this function

def Click():
	hello = "Hello " +entry.get()
	label = Label(root, text=hello)
	label.grid(row=2, column=0)

#Creating a text widget

label = Label(root, text="Label text using grid for placement")
label1 = Label(root, text="Label text using grid for placement")

#Showing it on the screen in the center top
#label.pack()

#Using the grid system:
label.grid(row=1, column=1)
label1.grid(row=0, column=0)

#Creating a button
#state=DISABLED disables a button
#padx or pady resizes buttons

button = Button(root, text="Enter your name", padx=50, pady=50, command=Click, fg="blue", bg="yellow")
button.grid(row=0, column=1)

button2 = Button(root, text="Now click me!")
button2.grid(row=1, column=0)

#Entry widged allows you to input data

entry = Entry(root, width=50)
entry.grid(row=3, column=0)
entry.get()
entry.insert(0, "Enter your name")

#End of the main loop
root.mainloop()
