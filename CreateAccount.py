#imports
import tkinter as tk 
import login as l
import sqlite3 as sql

#Main class 
class CreateAccount(tk.Frame):

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

        #Dictionary for dietary requirements
        self.diet = tk.StringVar(controller)
        self.reqs = {
            "None",
            "Egg Allergy",
            "Fish Allergy"
            "Peanut Allergy",
            "Shellfish Allergy",
            "Soy Allergy",
            "Tree Nut Allergy",
            "Wheat Allergy",
            "Vegetarian",
            "Vegan",
            "Kosher",
            "Halal"
        }
        self.diet.set("None")

        #dictionary for package level
        self.package = tk.StringVar(controller)
        self.packs = {
            "1",
            "2"
        }
        self.package.set("1")

        #Labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "EDIT ACCOUNT",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #First name 
        self.labelForename = tk.Label(
            self,
            text = "FORENAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
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
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
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
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
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
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
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
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
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
            text = "EMAIL",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelMail.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Forename 
        self.entryForename = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.entryForename.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Surname
        self.entrySurname = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.entrySurname.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Address
        self.entryAddress = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2
        )
        self.entryAddress.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Email
        self.entryMail = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2
        )
        self.entryMail.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #dropdowns

        #Package
        self.popPack = tk.OptionMenu(
            self,
            self.package,
            *self.packs
        )
        self.popPack.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Diet requirements
        self.popDiet = tk.OptionMenu(
            self,
            self.diet,
            *self.reqs
        )
        self.popDiet.grid(
            row = 5,
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
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            command = controller.show_frame(l.Login)
        )
        self.buttonReturn.grid(
            row = 7,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Save button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            command = self.updateAccount(
                self.entryForename.get(),
                self.entrySurname.get(),
                self.entryAddress.get(),
                self.package.get(),
                self.diet.get(),
                self.entryMail.get(),
            )
        )
        self.buttonSave.grid(
            row = 7,
            column = 1,
            sticky = "ns",
            padx = 10,
            pady = 10
        )

    def updateAccount(
        self,
        forename,
        surname,
        address,
        package,
        diet,
        email,
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        addForename = """INSERT INTO CLIENT (fname) VALUES (?)"""
        addSurname = """INSERT INTO CLIENT (sname) VALUES (?)"""
        addAddress = """INSERT INTO CLIENT (address) VALUES (?)"""
        addPackage = """INSERT INTO CLIENT (package) VALUES (?)"""
        addDiet = """INSERT INTO CLIENT (diet_req) VALUES (?)"""
        addEmail = """INSERT INTO CLIENT (email) VALUES (?)"""
        if not forename == None:
            if forename.isalpha() == True:
                cursor.execute(addForename, forename)
        if not surname == None:
            if surname.isalpha() == True:
                cursor.execute(addSurname, surname)
        if not address == None:
            if address[0:2].isdecimal() == True:
                if address[4:].isalpha() == True:
                    cursor.execute(addAddress, address)
        cursor.execute(addPackage, package)
        cursor.execute(addDiet, diet)
        if not email == None:
            if email.find("@")!=-1:
                if email[-5:].find(".")!=-1:
                    cursor.execute(addEmail, email)
        connection.commit()
        cursor.close()
