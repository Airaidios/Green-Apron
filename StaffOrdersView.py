#imports
import tkinter as tk
from tkinter.ttk import *
import sqlite3 as sql
import StaffOrder as so

#main class
class ActiveOrder(tk.Frame):

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


        #background colour
        self.configure(bg = "gray20")

        #Labels

        #Menu title Label
        self.label = tk.Label(
            self,
            text = "ACTIVE ORDERS",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.label.grid(
            row = 0,
            column = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Search bar
        self.entrySearch = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.entrySearch.grid(
            row = 5,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Search button
        self.buttonSearch = tk.Button(
            self,
            text = "SEARCH",
            fg = "#44d276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: self.searchOrder(
                self.entrySearch.get(),
                self.tree
            )
        )
        self.buttonSearch.grid(
            row = 5,
            column = 2,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #back button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(so.OrderPageStaff)
        )
        self.buttonReturn.grid(
            row = 10,
            column = 1,
            sticky = "ns",
            padx = 10,
            pady = 10
        )

        #Refresh table button
        self.buttonRefresh = tk.Button(
            self,
            text = "REFRESH",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.populateTable(self.tree)
        )
        self.buttonRefresh.grid(
            row = 10,
            column = 3,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Treeviews

        #active orders treeview, displays a readout of all records present in the order table.
        #Updated when "populateOrders" is called
        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            columns  = (
                "Client ID",
                "Kit"
            )
        )
        #Init different columns, as well as setting their titles
        self.tree.heading(
            "#0",
            text = "Order ID"
        )
        self.tree.heading(
            "#1",
            text = "Client ID"
        )
        self.tree.heading(
            "#2",
            text = "Kit ID"
        )
        self.tree.grid(
            row = 3,
            columnspan = 4,
            sticky = "ns"
        )
        #Adjust width of columns to reduce treeview size
        self.tree.column(
            "#0",
            minwidth = 50,
            width = 150
        )
        self.tree.column(
            "#1",
            minwidth = 50,
            width = 150
        )
        self.tree.column(
            "#2",
            minwidth = 50,
            width = 150
        )

        #Scrollbar for treeview
        self.scroll = tk.ttk.Scrollbar(
            self,
            orient = "vertical",
            command = self.tree.yview
        )
        self.scroll.grid(
            row = 3,
            columnspan = 4,
            sticky = "nse",
            pady = 10,
            padx = 10
        )
        self.tree.configure(yscrollcommand = self.scroll.set)

    #populate treeview with records from database
    def populateTable(
        self,
        table
    ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM ("ORDER")"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            table.insert(
                "",
                "end",
                text = str(i),
                values = (row[1], row[2])
            )
            i += 1
        connection.close()

    #Search through order table for term in any attribute
    def searchOrder(
        self,
        term,
        table
    ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        search = """SELECT * FROM "ORDER" WHERE (?) IN (order_id, client_id, kit_id)"""
        cursor.execute(search, (term,))
        i = 0
        for row in cursor.fetchall():
            table.insert(
                "",
                "end",
                text = str(i),
                values = (row[1], row[2])
            )
            i += 1
        connection.close()
