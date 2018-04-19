#imports
import tkinter as tk 
import Login as l
import sqlite3 as sql
import hashlib as hsh

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

        #Styling - set background colour
        self.configure(bg = "gray20")

        #Dictionary for dietary requirements, the items within this dictionary
        #will be used to populate a dropdown menu. This restriction of options
        #means that less validation will be needed
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
        #Set the default option of the dropdown to "None"
        self.diet.set("None")

        #Dictionary for options for package level.
        self.package = tk.StringVar(controller)
        self.packs = {
            "1",
            "2"
        }
        #Set default value
        self.package.set("1")

        #LABELS#

        #Menu title label
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

        #Label to identify username entry
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

        #Label to identify address entry
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

        #Label to identify the package dropdown
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

        #Label to identify the dietary requirements dropdown
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

        #Label to identify the email address entry
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

        #Label to identify the first password entry
        self.labelPass = tk.Label(
            self,
            text = "PASSWORD",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelPass.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Label to identify the second password entry
        self.labelConfirm = tk.Label(
            self,
            text = "CONFIRM PASSWORD",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelConfirm.grid(
            row = 7,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #ENTRIES#

        #Entry for username
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

        #Entry for address
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

        #Entry for email address
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

        #Initial entry for password
        self.entryPass = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25,
            show = "*"
        )
        self.entryPass.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Second entry for password - this is here to ensure
        #user enters the password they really want, and reduces the risk
        #of mistakes within the password
        self.entryConfirm = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25,
            show = "*"
        )
        self.entryConfirm.grid(
            row = 7,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #DROPDOWNS#

        #Package dropdown
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

        #Dietary requirements dropdown
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

        #BUTTONS#

        #Button to return to previous menu
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(l.Login)
        )
        self.buttonReturn.grid(
            row = 8,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Button to confirm account details and create an account by
        #calling the createAccount method
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.createAccount(
                self.entryUsername.get(),
                self.entryAddress.get(),
                self.package.get(),
                self.diet.get(),
                self.entryMail.get(),
                self.entryPass.get(),
                self.entryConfirm.get(),
                controller
            )
        )
        self.buttonSave.grid(
            row = 8,
            column = 1,
            sticky = "ns",
            padx = 10,
            pady = 10
        )

    #Method for taking entered details and collating them into one
    #record and insert that record into the Client table
    def createAccount(
        self,
        username,
        address,
        package,
        diet,
        email,
        password,
        password_confirm,
        controller
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        #Find most recently created record to insert level into
        fetchLatestRecord = """SELECT client_id FROM CLIENT ORDER BY client_id DESC LIMIT 1"""
        #Create record with validated data
        addData = """INSERT INTO CLIENT (username, address, package, diet_req, email, password) VALUES (?, ?, ?, ?, ?, ?)"""
        #Manually update most record with client access level
        insertLevel = """UPDATE CLIENT SET (level) = (?) WHERE (client_id) = ?"""
        #Hash password
        passwordhash = self.encryptPass(password)
        #Data to be inserted
        newData = (username, address, package, diet, email, passwordhash)
        if not username == None and username.isalpha() == True: #Username validation
            if not address == None and address[0:2].isdecimal() == True and address[4:].isalpha() == True: #Address validation
                if not package == None: #Package validation
                    if not diet == None: #Diet requirements validation
                        #Email address validation - I use a simple check here as the only way to ensure the address
                        #is correct is to send a confirmation email to the entered address
                        if not email == None and email.find("@") != -1 and email.find(".") != -1:
                            if password == password_confirm: #Ensure entered password is wanted password
                                cursor.execute(addData, newData) #Create populated record
                                cursor.execute(fetchLatestRecord) #Find the ID of that record
                                latestRecord = cursor.fetchone()[0] #Assign result of above execution to a variable
                                levelData = (0, latestRecord) #Define tuple to be inserted, this includes the client access level (0) and the most recent record ID (latestRecord)
                                cursor.execute(insertLevel, levelData) #Insert level into newest record
                                controller.show_frame(l.Login) #Bring user back to login menu
        connection.commit() #Save changes to database
        cursor.close() #Close connection

    #Method for encrypting password
    def encryptPass(
        self,
        password
    ):

        #Use hashlibs built in sha256 method to encrypt the password(which has to be formatted to utf-8)
        hashed = hsh.sha256(password.encode("utf-8")).hexdigest()
        return hashed