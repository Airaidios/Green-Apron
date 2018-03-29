#Imports
import tkinter as tk
import StaffOrder as so
import StaffStock as ss
import StaffFood as sf
import StaffAccount as sa
import Login as l

#Main class
class MainMenuStaff(tk.Frame):

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

        #Images

        #Logo
        self.logoLarge = tk.PhotoImage(file = controller.logo)
        self.logoScaled = self.logoLarge.subsample(
            3,
            3
        )

        #Labels

        #logo
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

        #Menu title label
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

        #Order management button

        self.buttonOrder = tk.Button(
            self,
            text = "ORDER MANAGEMENT",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(so.OrderPageStaff)
        )
        self.buttonOrder.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Stock management button
        self.buttonStock = tk.Button(
            self,
            text =
            "STOCK MANAGEMENT",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(ss.StockPage)
        )
        self.buttonStock.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Food menu management button
        self.buttonMenu = tk.Button(
            self,
            text = "MENU MANAGEMENT",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(sf.MenuPageStaff)
        )
        self.buttonMenu.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Account management menu button
        self.buttonAccount = tk.Button(
            self,
            text = "ACCOUNT MANAGEMENT",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(sa.StaffAccount)
        )
        self.buttonAccount.grid(
            row = 5,
            column = 1,
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
            width = 12,
            font = controller.SMALL_FONT,
            command = lambda: controller.destroy()
        )
        self.buttonQuit.grid(
            row = 6,
            column = 2,
            sticky = "nsw",
            pady = 10,
            padx = 10
        )

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
            row = 6,
            column = 0,
            sticky = "nse",
            pady = 10,
            padx = 10
        )
