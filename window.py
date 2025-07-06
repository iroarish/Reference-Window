import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps


class Window(Toplevel):

    def __init__(self, file_path):

        super().__init__()

        self.title("Reference")

        self.file_path = file_path

        self.geometry('300x300')

        self.label = ttk.Label(self)

        self.label.pack(fill=BOTH, expand=True)

        self.label.bind("<Configure>", self.fit_image)

        self.image_path = self.imageLocation()

        self.attributes('-topmost', True)

        print("CWD:", os.getcwd())

    def imageLocation(self):
        image_path = Image.open(self.file_path)
        return image_path

    def fit_image(self, event):
        self.image = ImageOps.contain(self.image_path, (event.width, event.height))
        new_image = self.image
        tk_image = ImageTk.PhotoImage(new_image)
        self.label.config(image=tk_image)
        self.label.image = tk_image
