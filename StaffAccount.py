#imports
import tkinter as tk
import StaffMainMenu as smm
import StaffAccountView as sav

#Main class
class StaffAccount(tk.Frame):

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

        #styling
        self.configure(bg = "gray20")

        #Labels

        #title
        self.labelTitle = tk.Label(
            self,
            text = "ACCOUNT MANAGEMENT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #buttons

        #View accounts button
        self.buttonRead = tk.Button(
            self,
            text = "VIEW ACCOUNTS",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(sav.StaffAccountView)
        )
        self.buttonRead.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

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
            command = lambda: controller.show_frame(smm.MainMenuStaff)
        )
        self.buttonReturn.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
