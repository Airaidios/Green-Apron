#imports
import tkinter as tk 
import sqlite3 as sql 
import ClientOrderMenu as com 

#main class 
class ClientOrderEdit(tk.Frame):

    #initialise method 
    def __init__(
        self,
        parent,
        controller
    ):

        #initialise frame
        tk.Frame.__init__(
            self,
            parent
        )

        #styling
        self.configure(bg = "gray20")

        #Labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "EDIT ORDER",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )