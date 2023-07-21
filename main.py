"""
Date:- July 20,2023
Developer:- Dinesh Singh

Descriptions: this application uses requests module which fetch two apis, first: gives coordinates of the given names. Second: uses output of first api and use this to give the result according to its weather condition.
"""

THEME_COLOR = "#75C2F6"
TEXT_COLOR = "#331D2C"
FRAME_COLOR = "#FBEEAC"
ENTRYBOX_COLOR = "#F4F2DE"
CANVAS_COLOR = FRAME_COLOR
TITTLE_FONT = "courier 24 bold"
FONT = "courier 12 bold"

from tkinter import *
from data import Data
from PIL import Image,ImageTk

class APP:
    def __init__(self):
        window = Tk()
        window.title("World's Weather")
        window.iconbitmap("AppICON.ico")
        window.config(bg=THEME_COLOR)
        window.geometry("400x400")
        Label(window, text="Weather Today!", fg=TEXT_COLOR, bg=THEME_COLOR, font=TITTLE_FONT) \
            .grid(row=0, column=0, padx=60, pady=20)
        frame = Frame(window, padx=20, pady=20, bg=FRAME_COLOR)
        frame.grid(row=1, column=0)
        Label(frame, text="CITY: ", fg=TEXT_COLOR, bg=FRAME_COLOR, font=FONT).grid(row=0, column=0, padx=10, pady=20)
        self.city_name = StringVar()
        self.city_name.set("")
        Entry(frame, textvariable=self.city_name, width=20, bg=ENTRYBOX_COLOR, fg=TEXT_COLOR, font=FONT).grid(row=0,
                                                                                                         column=1)
        Button(frame, text="GET INFORMARION", width=20, font=FONT, fg=TEXT_COLOR, bg=ENTRYBOX_COLOR,
               command=self.get_data).grid(row=1, column=0, columnspan=2)
        self.show = Label(frame, bg=FRAME_COLOR)
        self.show.grid(row=2, columnspan=2, column=0, pady=20)
        self.img = None
        window.mainloop()

    def get_data(self):
        # print(city_name.get())
        data = Data(self.city_name.get())
        if data.get_alert():
            img = "clear.gif"
        else:
            img = "rainy.gif"
        self.img = ImageTk.PhotoImage(Image.open(img).resize((150,120)))
        self.show.config(image=self.img)

APP()