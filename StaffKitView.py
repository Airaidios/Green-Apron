#imports
import tkinter as tk
from tkinter.ttk import *
import sqlite3 as sql
import StaffKitMenu as skm

#main class
class ViewKit(tk.Frame):

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
        self.titleLabel = tk.Label(
            self,
            text = "KITS",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.titleLabel.grid(
            row = 0,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Return button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(skm.StaffKitsMenu)
        )
        self.buttonReturn.grid(
            row = 10,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        self.buttonRefresh = tk.Button(
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
        self.buttonRefresh.grid(
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
                                                "Kit ID",
                                                "Kit Name",
                                                "Price",
                                                "Size"
                                                )
                                    )
        self.tree.heading(
                                    "#0",
                                    text = "Kit ID"
                                    )
        self.tree.heading(
                                    "#1",
                                    text = "Kit Name"
                                    )
        self.tree.heading(
                                    "#2",
                                    text = "Price"
                                    )
        self.tree.heading(
                                    "#3",
                                    text = "Size"
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
        #But first, clear tree so that duplicate records are not
        #displayed
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM KIT"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            table.insert(
                            "",
                            "end",
                            text = str(i),
                            values = (row[1], row[2], row[3])
                            )
            i += 1
