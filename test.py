from tkinter import *
from PIL import Image,ImageTk


root = Tk()

img = ImageTk.PhotoImage(Image.open("rainy.gif"))
Label(root,image=img).pack()
root.mainloop()