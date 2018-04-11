#Imports
import tkinter as tk
import ClientMainMenu as cmm 
import ClientAccountEdit as cae 
import ClientAccountView as cav 
import ClientDeleteCon as cadc

#main class 
class ClientAccountMenu(tk.Frame): 

    #Initialiser
    def __init__(
        self,
        parent,
        controller
    ):

        #Init frame 
        tk.Frame.__init__(
            self,
            parent
        )

        #Styling
        self.configure(background = "gray20")

        #Labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "ACCOUNT MANAGEMENT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20",
            width = 25
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Edit account
        self.buttonEdit = tk.Button(
            self,
            text = "EDIT ACCOUNT",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cae.ClientAccountEdit)
        )
        self.buttonEdit.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #View account details
        self.buttonView = tk.Button(
            self,
            text = "VIEW ACCOUNT DETAILS",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cav.ClientAccountView)
        )
        self.buttonView.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Delete account
        self.buttonDelete = tk.Button(
            self,
            text = "DELETE ACCOUNT",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cadc.ClientDeleteCon)
        )
        self.buttonDelete.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Return
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            font = controller.SMALL_FONT,
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cmm.MainMenuClient)
        )
        self.buttonReturn.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )