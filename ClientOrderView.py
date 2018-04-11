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
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Treeview

        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            columns = (
                "Account ID",
                "Kit ID"
            )
        )
        self.tree.heading(
            "#0",
            text = "Order ID"
        )
        self.tree.heading(
            "#1",
            text = "Account ID"
        )
        self.tree.heading(
            "#2",
            text = "Kit ID"
        )
        self.tree.grid(
            row = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Scrollbar for treeview
        self.scroll = tk.ttk.Scrollbar(
            self,
            orient = "vertical",
            command = self.tree.yview
        )
        self.scroll.grid(
            row = 1,
            columnspan = 2,
            sticky = "nse",
            pady = 10,
            padx = 10
        )
        self.tree.configure(yscrollcommand = self.scroll.set)

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
            column = 0,
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
                self.tree,
                controller.accountID
            )
        )
        self.buttonSearch.grid(
            row = 5,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

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
                controller.accountID
            )
        )
        self.buttonRefresh.grid(
            row = 10,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
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
        cursor.execute(insert, (aid,))
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

    def searchOrder(
        self,
        term,
        table,
        aid
    ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        search = """SELECT * FROM "ORDER" WHERE (?) IN (order_id, kit_id) AND (client_id) = ?"""
        Term = (term, aid)
        cursor.execute(search, Term)
        print(cursor.fetchall())
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