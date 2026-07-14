from tkinter import *

class Settings:
    """A class to maintain the all settings"""


    def __init__(self):

        #window
        self.window_width = 500
        self.window_height = 700
        
        #color 
        self.green = "#4de40c"
        self.light_green = "#b4f09b"
        self.light_green1 = "#cfe6c3"
        self.white = "#ffffff"
        self.dark_gray = "#4e4e4e"

        #image  
        self.done = PhotoImage(file="icons\\green_but.png")
        self.done = self.done.subsample(2,2)
        
        self.bin = PhotoImage(file="icons\\bin.png")
        self.bin = self.bin.subsample(2,2)
        
        self.main_icon = PhotoImage(file="icons\\to_do.png")
        self.main_icon = self.main_icon.subsample(2, 2)
