#imports
import tkinter as tk 
import sqlite3 as sql 
import ClientAccountMenu as cam 

#main class
class ClientAccountView(tk.Frame):

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

        #Styling
        self.configure(bg = "gray20")

        #Labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "VIEW ACCOUNT DETAILS",
            fg  = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Forename
        self.labelForename = tk.Label(
            self,
            text = "FORENAME",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelForename.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Surname
        self.labelSurname = tk.Label(
            self,
            text = "SURNAME",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelSurname.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Address
        self.labelAddress = tk.Label(
            self,
            text = "ADDRESS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelAddress.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Package
        self.labelPackage = tk.Label(
            self,
            text = "PACKAGE",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelPackage.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Diet requirements
        