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
        self.labelDiet = tk.Label(
            self,
            text = "DIET REQUIREMENTS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelDiet.grid(
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Email
        self.labelMail = tk.Label(
            self,
            text = "EMAIL ADDRESS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelMail.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Stringvars
        self.stringForename = tk.StringVar()
        self.stringSurname = tk.StringVar()
        self.stringAddress = tk.StringVar()
        self.stringPackage = tk.StringVar()
        self.stringDiet = tk.StringVar()
        self.stringMail = tk.StringVar()

        #Display Labels

        #Forename display
        self.displayForename = tk.Label(
            self,
            text = self.stringForename,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.displayForename.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Surname display
        self.displaySurname = tk.Label(
            self,
            text = self.stringSurname,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displaySurname.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Address display
        self.displayAddress = tk.Label(
            self,
            text = self.stringAddress,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.displayAddress.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Package display
        self.displayPackage = tk.Label(
            self,
            text = self.stringPackage,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayPackage.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Diet display
        self.displayDiet = tk.Label(
            self,
            text = self.stringDiet,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayDiet.grid(
            row = 5, 
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Mail display
        self.displayMail = tk.Label(
            self,
            text = self.stringMail,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayMail.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
        