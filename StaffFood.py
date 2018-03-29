#imports
import tkinter as tk
import StaffKitMenu as skm
import StaffMainMenu as smm
import StaffRecipeMenu as srm


#main class
class MenuPageStaff(tk.Frame):

    #initialise Method
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

        #Labels

        #Title
        self.label = tk.Label(
            self,
            text = "MENU MANAGEMENT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.label.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Kit button
        self.kitButton = tk.Button(
            self,
            text = "KITS",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda:controller.show_frame(skm.StaffKitsMenu)
        )
        self.kitButton.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Recipe button
        self.recipeButton = tk.Button(
            self,
            text = "RECIPES",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(srm.StaffRecipeMenu)
        )
        self.recipeButton.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Return button
        self.returnButton = tk.Button(
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
        self.returnButton.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
