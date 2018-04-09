#Imports
import tkinter as tk
import ClientOrderMenu as com 
import ClientFoodView as cfv 
import ClientAccountMenu as cam 
import Login as l

#Main Class
class MainMenuClient(tk.Frame):

    #Initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        #Initialise Frame
        tk.Frame.__init__(
            self,
            parent
        )

        #Styling
        self.configure(background = "gray20")

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
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Menu Title Label 
        self.titleLabel = tk.Label(
            self,
            text = "MAIN MENU",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.titleLabel.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons 

        #Order Menu Button 

        self.buttonOrder = tk.Button(
            self,
            text = "ORDER MANAGEMENT",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(com.ClientOrderMenu)
        )
        self.buttonOrder.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Food Menu
        self.buttonFood = tk.Button(
            self,
            text = "BROWSE MENUS",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cfv.ClientFoodView)
        )
        self.buttonFood.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Account Menu
        self.buttonAccount = tk.Button(
            self,
            text = "ACCOUNT MANAGEMENT",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cam.ClientAccountMenu)
        )
        self.buttonAccount.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Logout Button
        self.buttonLogout = tk.Button(
            self,
            text = "LOGOUT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 12,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(l.Login)
        )
        self.buttonLogout.grid(
            row = 5,
            column = 0,
            sticky = "nse",
            pady = 10,
            padx = 10
        )

        #Quit Button
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
            row = 5,
            column = 2,
            sticky = "nsw",
            pady = 10,
            padx = 10
        )