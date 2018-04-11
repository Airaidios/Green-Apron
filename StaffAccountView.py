#imports
import tkinter as tk
import StaffAccount as sa
import sqlite3 as sql

#main class
class StaffAccountView(tk.Frame):

    #initialise Method
    def __init__(
        self,
        parent,
        controller
    ):

        #Initialise frames
        tk.Frame.__init__(
            self,
            parent
        )

        #styling
        self.configure(bg = "gray20")

        #labels

        #Title
        self.label = tk.Label(
            self,
            text = "ACCOUNTS",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.label.grid(
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
            command = lambda: controller.show_frame(sa.StaffAccount)
        )
        self.buttonReturn.grid(
            row = 10,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Refresh table contents button
        self.buttonRefresh = tk.Button(
            self,
            text = "REFRESH",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.populateInfo(self.tree)
        )
        self.buttonRefresh.grid(
            row = 10,
            column = 2,
            columnspan = 2,
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
                "Account ID",
                "Order ID",
                "Username",
                "Address",
                "Package",
                "Diet Reqs",
                "Email",
                "Level"
            )
        )
        self.tree.heading(
            "#0",
            text = "Account ID"
        )
        self.tree.heading(
            "#1",
            text = "Username"
        )
        self.tree.heading(
            "#2",
            text = "Address",
        )
        self.tree.heading(
            "#3",
            text = "Package",
        )
        self.tree.heading(
            "#4",
            text = "Diet Reqs",
        )
        self.tree.heading(
            "#5",
            text = "Email",
        )
        self.tree.heading(
            "#6",
            text = "Level"
        )
        self.tree.column(
            "#0",
            minwidth = 50,
            width = 50
        )
        self.tree.column(
            "#1",
            minwidth = 100,
            width = 100
        )
        self.tree.column(
            "#2",
            minwidth = 100,
            width = 150
        )
        self.tree.column(
            "#3",
            minwidth = 50,
            width = 50
        )
        self.tree.column(
            "#4",
            minwidth = 100,
            width = 100
        )
        self.tree.column(
            "#5",
            minwidth = 100,
            width = 150
        )
        self.tree.column(
            "#6",
            minwidth = 50,
            width = 50
        )
        self.tree.grid(
            row = 3,
            columnspan = 3,
            sticky = "ns"
        )
    
    def populateInfo(
        self,
        table
    ):
        #populate treeview with records from database
        connection = sql.connect("ga.db") 
        cursor = connection.cursor()
        insert = """SELECT * FROM ("CLIENT")"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            self.tree.insert(
                "",
                "end",
                text = str(i),
                values = (row[1], row[2], row[3], row[4], row[5], row[6])
            )
            i += 1
