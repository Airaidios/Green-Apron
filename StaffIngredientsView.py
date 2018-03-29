#imports
import tkinter as tk
from tkinter.ttk import *
import sqlite3 as sql
import StaffStock as ss

#main class
class ViewIngredients(tk.Frame):
    
    #Initialise method
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

        #background colour
        self.configure(bg = "gray20")

        #Labels

        #Title
        self.titleLabel = tk.Label(
            self,
            text = "VIEW INGREDIENTS",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.titleLabel.grid(
            row = 0,
            column = 1,
            columnspan = 3,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Return
        self.returnButton = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(ss.StockPage)
        )
        self.returnButton.grid(
            row = 10,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Refresh
        self.refreshButton = tk.Button(
            self,
            text = "REFRESH",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.updateTable(self.tree)
        )
        self.refreshButton.grid(
            row = 10,
            column = 4,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Treeview

        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            columns  = (
                "Ingredient ID",
                "Name",
                "Quantity",
                "Allergen",
                "Type"
            )
        )
        self.tree.heading(
            "#0",
            text = "Ingredient ID"
        )
        self.tree.heading(
            "#1",
            text = "Name"
        )
        self.tree.heading(
            "#2",
            text = "Quantity"
        )
        self.tree.heading(
            "#3",
            text = "Allergen"
        )
        self.tree.heading(
            "#4",
            text = "Type"
        )
        self.tree.grid(
            row = 3,
            columnspan = 5,
            sticky = "ns"
        )

    #update treeview
    def updateTable(
        self,
        tree 
    ):
        tree.delete(*tree.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM INGREDIENT"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            tree.insert(
                "",
                "end",
                text = str(i),
                values = (row[1], row[2], row[3], row[4])
            )
            i += 1  