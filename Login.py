#Imports
import tkinter as tk
import StaffMainMenu as smm
import ClientMainMenu as cmm
import sqlite3 as sql
import CreateAccount as ca
import hashlib as hsh

#Main class
class Login(tk.Frame):

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

        #Styling - set window background
        self.configure(background = "gray20")

        #Images

        #Logo, scaled down to fit within window.
        self.logoLarge = tk.PhotoImage(file = controller.logo)
        self.logoScaled = self.logoLarge.subsample(
            3,
            3
        )

        #LABELS#

        #Label that contains logo
        self.logoLabel = tk.Label(
            self,
            bg = "gray20",
            image = self.logoScaled
        )
        self.logoLabel.image = self.logoScaled
        self.logoLabel.grid(
            row = 0,
            column = 1,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #Menu title label
        self.label = tk.Label(
            self,
            text = "LOGIN",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.label.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Label to identify entry for usernames
        self.labelName = tk.Label(
            self,
            text = "USERNAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelName.grid(
            row = 2,
            column = 0,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #Label to identify entry for passwords
        self.labelPass = tk.Label(
            self,
            text = "PASSWORD",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelPass.grid(
            row = 3,
            column = 0,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #ENTRIES#

        #Entry for username
        self.entryName = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white"
        )
        self.entryName.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entry for passwords
        self.entryPass = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white",
            show = "*" #this replaces anything entered into the field with a string of *'s
        )
        self.entryPass.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #BUTTONS#

        #Login button
        self.buttonLogin = tk.Button(
            self,
            text = "LOGIN",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            command = lambda: self.checkPass(
                self.entryPass.get(),
                self.entryName.get(),
                controller,
                ca.CreateAccount
            )
        )
        self.buttonLogin.grid(
            row = 4,
            column = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Quit button
        self.buttonQuit = tk.Button(
            self,
            text = "EXIT",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.destroy()
        )
        self.buttonQuit.grid(
            row = 4,
            column = 0,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #Button for creating an account
        self.buttonCreate = tk.Button(
            self,
            text = "CREATE ACCOUNT",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(ca.CreateAccount)
        )
        self.buttonCreate.grid(
            row = 5,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for validating password.
    def checkPass(
        self,
        password,
        username,
        controller,
        ca
    ):
        connection = sql.connect("ga.db") #Establish connection to central database
        cursor = connection.cursor() #Initialise a cursor
        #Execute a non-predefined SQL statement for finding the password associated with
        #entered username - This password is encrypted using 256bit encryption to prevent
        #unauthorised access.
        cursor.execute("""SELECT password FROM CLIENT WHERE username = ?""", (username,))
        passwordfetched = cursor.fetchone()[0] #Assign found password to a variable
        passwordhash = hsh.sha256(password.encode("utf-8")).hexdigest() #Encrypt entered password using 256bit encryption
        if passwordhash == passwordfetched: #Compare the encrypted passwords
            #If both encrypted passwords are the same, run the login method from Main
            controller.login(
                self.entryName.get(),
                self.entryPass.get(),
                controller,
                controller.accountID
            )
        connection.close() #Close database connection
