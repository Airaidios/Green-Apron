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
            "Fish Allergy",
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
        self.labelUsername = tk.Label(
            self,
            text = "USERNAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelUsername.grid(
            row = 1,
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
            row = 2,
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
            row = 3,
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
            row = 4,
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
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #username 
        self.entryUsername = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2,
            width = 25
        )
        self.entryUsername.grid(
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
            bd = 2,
            width = 25
        )
        self.entryAddress.grid(
            row = 2,
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
            bd = 2,
            width = 25
        )
        self.entryMail.grid(
            row = 5,
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
            row = 3,
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
            row = 4,
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

        #Save button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.updateAccount(
                self.entryUsername.get(),
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

    #Update account details
    def updateAccount(
        self,
        username,
        address,
        package,
        diet,
        email,
        aid
    ):
        #Create tuples that contain the new data and the accountID
        Username = (username, aid)
        Address = (address, aid)
        Package = (package, aid)
        Diet = (diet, aid)
        Email = (email, aid)
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        #Update username in Client table where the client ID is equal to the contents of the Account ID token
        addusername = """UPDATE CLIENT SET (username) = (?) WHERE (client_id) = ?"""
        #Update address in Client table where the client ID is equal to the contents of the Account ID token
        addAddress = """UPDATE CLIENT SET (address) = (?) WHERE (client_id) = ?"""
        #Update package in Client table where the client ID is equal to the contents of the Account ID token
        addPackage = """UPDATE CLIENT SET (package) = (?) WHERE (client_id) = ?"""
        #Update dietary requirements in Client table where the client ID is equal to the contents of the Account ID token
        addDiet = """UPDATE CLIENT SET (diet_req) = (?) WHERE (client_id) = ?"""
        #Update email address in Client table where the client ID is equal to the contents of the Account ID token
        addEmail = """UPDATE CLIENT SET (email) = (?) WHERE (client_id) = ?"""
        if not username == None: #username presence check
            if username.isalpha() == True: #username type check
                cursor.execute(addusername, Username) #Execute update
        if not address == None: #Address presence check
            if address[0:2].isdecimal() == True: #Address type check
                if address[4:].isalpha() == True: #Address format check
                    cursor.execute(addAddress, Address) #Execute update
        if not email == None: #Email presence check
            if email.find(".") != -1: #Email format check
                if email.find("@") != -1:
                    cursor.execute(addEmail, Email) #Execute update
        cursor.execute(addPackage, Package) #Execute package update
        cursor.execute(addDiet, Diet) #Execute dietary requirements update
        connection.commit() #close connection
        cursor.close() #close cursor