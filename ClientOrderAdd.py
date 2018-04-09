#imports
import ClientOrderMenu as com 
import sqlite3 as sql 
import tkinter as tk 

#main class
class ClientOrderAdd(tk.Frame):

    #Initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        #Initialise frame
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
            text = "PLACE ORDER",
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

        