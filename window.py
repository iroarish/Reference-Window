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

        self.canvas = Canvas(self)

        self.canvas.pack(fill=BOTH, expand=True)

        self.canvas.bind("<Configure>", self.fit_image)

        self.zoom_lvl= 1

        self.canvas.bind("<MouseWheel>", self.zoom_func)

        self.canvas.bind("<ButtonPress-2>", self.start_panning)

        self.canvas.bind("<B2-Motion>", self.do_panning)

        self.canvas.bind("<ButtonRelease-2>", self.end_panning)

        self.image_path = self.imageLocation()

        self.attributes('-topmost', True)

        self.do_resize = None

    def imageLocation(self):

        image_path = Image.open(self.file_path)

        return image_path

    def fit_image(self, event):

        if self.do_resize:

            self.after_cancel(self.do_resize)

        def resize_window():

            self.image = ImageOps.contain(self.image_path, (event.width, event.height))

            self.aspect_ratio = self.image.width / self.image.height

            self.window_resize()

            new_image = self.image

            self.tk_image = ImageTk.PhotoImage(new_image)

            self.canvas.create_image(0, 0, anchor=NW, image=self.tk_image)

            self.canvas.image = self.tk_image

            self.do_resize = None

        self.do_resize = self.after(200, resize_window)      

    def window_resize(self):

        if self:

            width = self.image.width

            height = int(self.image.width / self.aspect_ratio)

            self.geometry(f"{width}x{height}")

    def zoom_func(self, event):

        print(event.delta, self.zoom_lvl)

        if event.delta > 0:
            self.zoom_lvl *= 1.1
        elif self.zoom_lvl <= 1:
            self.zoom_lvl = 1
        else:
            self.zoom_lvl /= 1.1

        w, h = self.image.size

        print(w, h)

        zoom_img = (int(w * self.zoom_lvl), int(h * self.zoom_lvl))

        zoomed_in = self.image.resize(zoom_img, Image.LANCZOS)

        print(zoomed_in)

        self.tk_image = ImageTk.PhotoImage(zoomed_in)
        
        self.canvas.delete("all")

        self.canvas.create_image(0, 0, anchor=NW, image=self.tk_image)

        self.canvas.image = self.tk_image

    def start_panning(self, event):
        self.canvas.config(cursor="fleur")
        self._pan_start = (event.x, event.y)

    def do_panning(self, event):
        if self._pan_start:
            dx = event.x - self._pan_start[0]
            dy = event.y - self._pan_start[1]
            self.canvas.move("all", dx, dy)
            self._pan_start = (event.x, event.y)

    def end_panning(self, event):
        self.canvas.config(cursor="")
        self._pan_start = None
