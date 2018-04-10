#imports
import tkinter as tk 
import ClientAccountMenu as cam 
import sqlite3 as sql

#Main class 
class ClientAccountEdit(tk.Frame):

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
        self.labelusername = tk.Label(
            self,
            text = "username",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelusername.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #
        self.label = tk.Label(
            self,
            text = "",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.label.grid(
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

        #username 
        self.entryusername = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.entryusername.grid(
            row = 1,
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
            command = lambda: controller.show_frame(cam.ClientAccountMenu)
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
                self.entryusername.get(),
                self.entryAddress.get(),
                self.package.get(),
                self.diet.get(),
                self.entryMail.get(),
                controller.accountID
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
        username,
        address,
        package,
        diet,
        email,
        aid
    ):
        Username = (username, aid)
        Address = (address, aid)
        Package = (package, aid)
        Diet = (diet, aid)
        Email = (email, aid)
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        addusername = """UPDATE CLIENT SET (fname) = (?) WHERE (client_id) = ?"""
        addAddress = """UPDATE CLIENT SET (address) = (?) WHERE (client_id) = ?"""
        addPackage = """UPDATE CLIENT SET (package) = (?) WHERE (client_id) = ?"""
        addDiet = """UPDATE CLIENT SET (diet_req) = (?) WHERE (client_id) = ?"""
        addEmail = """UPDATE CLIENT SET (email) = (?) WHERE (client_id) = ?"""
        if not username == None:
            if username.isalpha() == True:
                cursor.execute(addusername, Username)
        if not address == None:
            if address.isalpha() == True:
                cursor.execute(addAddress, Address)
        if not email == None:
            if email.isalpha() == True:
                cursor.execute(addEmail, Email)
        cursor.execute(addPackage, Package)
        cursor.execute(addDiet, Diet)
        connection.commit()
        cursor.close()