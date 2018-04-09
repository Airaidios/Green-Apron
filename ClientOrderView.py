#imports
import tkinter as tk 
from tkinter.ttk import * 
import sqlite3 as sql 
import ClientOrderMenu as com 

#main class 
class ClientOrderView(tk.Frame):

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

        #labels

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "YOUR ORDERS",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT,
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Treeview

        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            columns = (
                "Kit"
            )
        )
        self.tree.heading(
            "#0",
            text = "Order ID"
        )
        self.tree.heading(
            "#1",
            text = "Kit"
        )
        self.tree.grid(
            row = 1,
            columnspan = 3,
            sticky = "ns"
        )

        #Buttons

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
            command = lambda: controller.show_frame(com.ClientOrderMenu)
        )
        self.buttonReturn.grid(
            row = 10,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Refresh button
        self.buttonRefresh = tk.Button(
            self,
            text = "REFRESH",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.populateTable(
                self.tree,
                accountID
            )
        )

    #refresh table
    def populateTable(
        self,
        table,
        aid
    ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM ("ORDER") WHERE (client_id) = ?"""
        cursor.execute(insert, aid)
        i = 0
        for row in cursor:
            table.insert(
                "",
                "end",
                text = str(i),
                values = (row[1])
            )
            i += 1