#imports
import tkinter as tk 
from tkinter.ttk import * 
import sqlite3 as sql 
import ClientOrderMenu as com 

#main class 
class ClientOrderView(tk.Frame):

    #initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        #initialise frames 
        tk.Frame.__init__(
            self,
            parent
        )

        #styling
        self.configure(bg = "gray20")

        #labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "YOUR ORDERS",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT,
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        