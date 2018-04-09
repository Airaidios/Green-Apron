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

        #Display Labels

        #Forename display
        self.displayForename = tk.Label(
            self,
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

        #Buttons

        #Return button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(cam.ClientAccountMenu)
        )
        self.buttonReturn.grid(
            row = 7,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Refresh button
        self.buttonRefresh = tk.Button(
            self,
            text = "REFRESH",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: self.updateDetails(
                self.displayForename,
                self.displaySurname,
                self.displayAddress,
                self.displayPackage,
                self.displayDiet,
                self.displayMail,
                accountID
            )
        )
        self.buttonRefresh.grid(
            row = 7,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
        
    def updateDetails(
        self,
        forenamedisplay,
        surnamedisplay,
        addressdisplay,
        packagedisplay,
        dietdisplay,
        maildisplay,
        aid
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        fetchForename = """SELECT fname FROM CLIENT WHERE client_id = ?"""
        fetchSurname = """SELECT sname FROM CLIENT WHERE client_id = ?"""
        fetchAddress = """SELECT address FROM CLIENT WHERE client_id = ?"""
        fetchPackage = """SELECT package FROM CLIENT WHERE client_id = ?"""
        fetchDiet = """SELECT diet_req FROM CLIENT WHERE client_id = ?"""
        fetchMail = """SELECT email FROM CLIENT WHERE client_id = ?"""
        Forename = cursor.execute(fetchForename, aid)
        Surname = cursor.execute(fetchSurname, aid)
        Address = cursor.execute(fetchAddress, aid)
        Package = cursor.execute(fetchPackage, aid)
        Diet = cursor.execute(fetchDiet, aid)
        Mail = cursor.execute(fetchMail, aid)
        forenamedisplay.configure(text = Forename)
        surnamedisplay.configure(text = Surname)
        addressdisplay.configure(text = Address)
        packagedisplay.configure(text = Package)
        dietdisplay.configure(text = Diet)
        maildisplay.configure(text = Mail)