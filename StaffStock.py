#imports
import tkinter as tk
import StaffIngredientAdd as sia
import StaffIngredientEdit as sie
import StaffMainMenu as smm
import StaffIngredientsView as siv
import sqlite3 as sql

#main class
class StockPage(tk.Frame):

    #initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        #initialise frame
        tk.Frame.__init__(
            self,
            parent
        )

        #Styling
        self.configure(bg = "gray20")

        #Labels

        #Menu title label
        self.label = tk.Label(
            self,
            text = "STOCK MANAGEMENT",
            bg = "gray20",
            fg = "white",
            width = 25,
            font = controller.LARGE_FONT
        )
        self.label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #ID entry
        self.ingEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.ingEntry.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Add ingredient menu button
        self.buttonAddIngredient = tk.Button(
            self,
            text = "ADD INGREDIENT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "palegreen",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(sia.AddIngredient)
        )
        self.buttonAddIngredient.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Edit ingredient menu button
        self.buttonEditIngredient = tk.Button(
            self,
            text = "EDIT INGREDIENT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(sie.EditIngredient)
        )
        self.buttonEditIngredient.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
        
        self.buttonView = tk.Button(
            self,
            text = "VIEW INGREDIENTS",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(siv.ViewIngredients)
        )
        self.buttonView.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        self.buttonDelete = tk.Button(
            self,
            text = "DELETE INGREDIENT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: self.deleteIng(self.ingEntry.get())
        )
        self.buttonDelete.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Back button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(smm.MainMenuStaff)
        )
        self.buttonReturn.grid(
            row = 10,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    def deleteIng(
        self,
        iid,
    ):
        #Establish connection to central database
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        #Statement for checking whether the entered ID exists
        select = """SELECT order_id FROM INGREDIENT WHERE ing_id = ?"""
        cursor.execute(
            select,
            (iid,)
        )
        if iid.isdecimal() == True:
            if cursor.fetchone():
                #Statement for deleting the relevant record
                delete = """DELETE FROM INGREDIENT WHERE ing_id = ?"""
                cursor.execute(
                    delete,
                    iid
                )
                #"Save changes"
                connection.commit()
            else:
                pass
        else:
            pass
