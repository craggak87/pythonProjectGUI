from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("960x540")
root.iconbitmap('ico/netfol.ico')
root.title("Frames")

topframe = LabelFrame(root, width=960, height=200, padx=100, pady=100, relief=GROOVE ,bg='green')
topframe.pack()

mainframe = LabelFrame(root, width=960, height=300, bd=2, padx=100, pady=100, relief=SUNKEN, bg='red')
mainframe.pack()

menu = Button(topframe, text="Menu", padx=5, pady=5)
menu.pack(anchor=W)
menu2 = Button(topframe, text="Menu2", padx=5, pady=5)
menu.pack()
menu3 = Button(topframe, text="Menu3", padx=5, pady=5)
menu.pack()

root.mainloop()
