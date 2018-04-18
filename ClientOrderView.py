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

        #Styling - set background colour
        self.configure(bg = "gray20")

        #LABELS#

        #Menu title label
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

        #TREEVIEWS#

        #Treeview to display orders owned by the user
        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            columns = (
                "Account ID",
                "Kit ID"
            )
        )
        #Initialise headings
        #First heading contains order_id
        self.tree.heading(
            "#0",
            text = "Order ID"
        )
        #Second heading contains account_id
        self.tree.heading(
            "#1",
            text = "Account ID"
        )
        #Third heading contains kit_id
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
        self.tree.configure(yscrollcommand = self.scroll.set) #Set the movement of the scrollbar
        #to manipulate the vertical scrolling of the treeview

        #ENTRIES#

        #Search bar entry
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

        #BUTTONS#

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

    #Refresh contents of table - allows live updates to the database readout
    def populateTable(
        self,
        table,
        aid
    ):
        table.delete(*table.get_children()) #Deletes previous contents of treeview to
        #prevent duplicate records, but this also means the table is empty when first
        #viewing after starting program.
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        #SQL statement to fetch records in the Order table belonging to the user
        insert = """SELECT * FROM ("ORDER") WHERE (client_id) = ?"""
        cursor.execute(insert, (aid,)) #Execute fetch
        i = 0 #Init iterator
        for row in cursor: #Begin iteration through contents of cursor
            table.insert( #Insert currently selected row into table 
                "",
                "end",
                text = str(i),
                values = (row[1], row[2])
            )
            i += 1 #Increase counter
        connection.close() #Close connection

    #Take search term and return all rows in the table containing the search term
    def searchOrder(
        self,
        term,
        table,
        aid
    ):
        table.delete(*table.get_children()) #Clear contents of treeview to make room for search results
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        #SQL statement that runs through every attribute in every record owned by the user and searches it for the search term
        search = """SELECT * FROM "ORDER" WHERE ((?) IN (order_id, kit_id)) AND (client_id) = ?"""
        Term = (int(term), aid) #Create tuple that contains the search term and account ID
        cursor.execute(search, Term) #Execute search
        i = 0 #init counter
        for row in cursor.fetchall(): #Iterate through the cursor
            table.insert( #Insert into the treeview the currently selected row in the cursor
                "",
                "end",
                text = str(i),
                values = (row[1], row[2])
            )
            i += 1 #increase counter
        connection.close() #Close connection