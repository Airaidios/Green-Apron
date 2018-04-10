#Imports
import tkinter as tk
import StaffMainMenu as smm
import ClientMainMenu as cmm
import sqlite3 as sql
import CreateAccount as ca

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

        #Styling
        self.configure(background = "gray20")

        #Initialise infoString for use in infoLabel
        self.infoString = ""

        #Images

        #Logo
        self.logoLarge = tk.PhotoImage(file = controller.logo)
        self.logoScaled = self.logoLarge.subsample(
            3,
            3
        )

        #Labels

        #Logo
        self.logoLabel = tk.Label(
            self,
            bg = "gray20",
            image = self.logoScaled
        )
        self.logoLabel.image = self.logoScaled
        self.logoLabel.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #Title label
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

        #Username label
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

        #Password label
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

        #Label for info like "incorrect password", etc.
        self.labelInfo = tk.Label(
            self,
            text = self.infoString,
            font = controller.SMALL_FONT,
            fg = "#FF0059",
            bg = "gray20"
        )
        self.labelInfo.grid(
            row = 5,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Username entry
        self.entryName = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white"
        )
        self.entryName.grid(
            row = 2,
            column = 2,
            sticky = "nsw",
            pady = 10,
            padx = 10
        )


        #Password entry
        self.entryPass = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white",
            show = "*" #this replaces anything entered into the field with a string of *'s
        )
        self.entryPass.grid(
            row = 3,
            column = 2,
            sticky = "nsw",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Login button
        self.buttonLogin = tk.Button(
            self,
            text = "LOGIN",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 12,
            command = lambda: controller.login(
               self.entryName.get(),
               self.entryPass.get(),
               controller,
               controller.accountID
            )
        )
        self.buttonLogin.grid(
            row = 4,
            column = 2,
            sticky = "nsw",
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
            width = 12,
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
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        
