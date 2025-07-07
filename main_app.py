import os
import sys
from tkinter import *
from tkinter import ttk
from window import Window
from tkinterdnd2 import TkinterDnD, DND_FILES

class App:

    def __init__(self):

        self.root = TkinterDnD.Tk()

        self.root.title("Reference Window App")

        self.icon = self.resource_path("assets/app.ico")

        self.root.iconbitmap(self.icon)
        
        self.root.attributes("-topmost", True)

        self.root.geometry("250x100")

        self.root.resizable(False, False)

        self.container = Frame(self.root)

        self.container.pack(expand=True)

        self.label = ttk.Label(self.container, text="Drag and Drop to Add Photo References")

        self.label.pack()

        # self.button = ttk.Button(self.container, text="Add", width=200, command=Window)

        # self.button.pack()

        self.root.drop_target_register(DND_FILES)

        self.root.dnd_bind('<<Drop>>', self.drop)

        self.root.mainloop()
    
    def drop(self, event):
        file_list = self.root.tk.splitlist(event.data)

        for file_path in file_list:
            file_path = file_path.strip('{}')
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                Window(file_path)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)