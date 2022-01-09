# Import everything from the tkinter module

from tkinter import *

# Start of the main loop

root = Tk()

# Window title

root.title("Simple calculator")

# Entry field
entry = Entry(root, width=45, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button function

def button_click(number):
	#entry.delete(0, END)
	current = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(current) + str(number))

def button_clear():
	entry.delete(0, END)

def button_add():
	first_number = entry.get()
	global f_num
	global math
	math = "add"
	f_num = int(first_number)
	entry.delete(0, END)

def button_eq():
	second_number = entry.get()
	entry.delete(0, END)

	if math == "add":
		entry.insert(0, f_num + int(second_number))

	if math == "sub":
		entry.insert(0, f_num - int(second_number))

	if math == "mul":
		entry.insert(0, f_num * int(second_number))

	if math == "div":
		entry.insert(0, f_num / int(second_number))

def button_sub():
	first_number = entry.get()
	global f_num
	global math
	math = "sub"
	f_num = int(first_number)
	entry.delete(0, END)

def button_mul():
	first_number = entry.get()
	global f_num
	global math
	math = "mul"
	f_num = int(first_number)
	entry.delete(0, END)

def button_div():
	first_number = entry.get()
	global f_num
	global math
	math = "div"
	f_num = int(first_number)
	entry.delete(0, END)

# Buttons

button_add = Button(root, text="+", padx=40, pady=40, command=button_add)
button_0 = Button(root, text="0", padx=40, pady=40, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=40, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=40, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=40, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=40, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=40, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=40, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=40, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=40, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=40, command=lambda: button_click(9))
button_clr = Button(root, text="C", padx=40, pady=40, command=button_clear)
button_eq = Button(root, text="=", padx=40, pady=40, command=button_eq)
button_sub = Button(root, text="-", padx=40, pady=40, command=button_sub)
button_mul = Button(root, text="*", padx=40, pady=40, command=button_mul)
button_div = Button(root, text="/", padx=40, pady=40, command=button_div)

button_add.grid(row=1, column=3)
button_0.grid(row=4, column=1)
button_clr.grid(row=4, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_eq.grid(row=4, column=0)




#End of the main loop
root.mainloop()
