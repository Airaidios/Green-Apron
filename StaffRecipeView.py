#imports
import tkinter as tk
from tkinter.ttk import *
import sqlite3 as sql
import StaffRecipeMenu as srm

#main class
class StaffRecipeView(tk.Frame):

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

        #Title label
        label = tk.Label(
                            self,
                            text = "RECIPES",
                            font = controller.LARGE_FONT,
                            fg = "white",
                            bg = "gray20"
                            )
        label.grid(
                            row = 0,
                            column = 1,
                            columnspan = 2,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Buttons

        #Return button
        buttonReturn = tk.Button(
                                    self,
                                    text = "RETURN",
                                    fg = "#44D276",
                                    bg = "gray10",
                                    activeforeground = "white",
                                    activebackground = "#44D276",
                                    width = 25,
                                    font = controller.SMALL_FONT,
                                    command = lambda: controller.show_frame(srm.StaffRecipeMenu)
                                    )
        buttonReturn.grid(
                                    row = 10,
                                    column = 0,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #Refresh button
        buttonRefresh = tk.Button(
                                    self,
                                    text = "REFRESH",
                                    fg = "#44D276",
                                    bg = "gray10",
                                    activeforeground = "#44D276",
                                    activebackground = "white",
                                    width = 25,
                                    font = controller.SMALL_FONT,
                                    command = lambda: self.updateTable(self.tree)
                                    )
        buttonRefresh.grid(
                                    row = 10,
                                    column = 3,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #Treeview

        #Kits treeview
        self.tree = tk.ttk.Treeview(
                                    self,
                                    style = "Custom.Treeview",
                                    columns = (
                                                "Recipe ID",
                                                "Recipe Name",
                                                "Culture",
                                                "Servings",
                                                "Prep Time"
                                                )
                                    )
        self.tree.heading(
                                    "#0",
                                    text = "Recipe ID"
                                    )
        self.tree.heading(
                                    "#1",
                                    text = "Recipe Name"
                                    )
        self.tree.heading(
                                    "#2",
                                    text = "Culture"
                                    )
        self.tree.heading(
                                    "#3",
                                    text = "Servings"
                                    )
        self.tree.heading(
                                    "#4",
                                    text = "Prep Time"
                                    )
        self.tree.grid(
                                    row = 3,
                                    columnspan = 4,
                                    sticky = "ns"
                                    )

    def updateTable(
                    self,
                    table 
                    ):
    #populate treeview with records from database
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM ("RECIPE")"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            table.insert(
                            "",
                            "end",
                            text = str(i),
                            values = (row[1], row[2], row[3], row[4])
                            )
            i += 1
