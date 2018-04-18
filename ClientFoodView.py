#imports
import tkinter as tk
from tkinter.ttk import *
import ClientMainMenu as cmm 
import sqlite3 as sql

#main class 
class ClientFoodView(tk.Frame): 

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

        #Styling 
        self.configure(bg = "gray20")

        #LABELS#

        #Title label 
        self.titleLabel = tk.Label(
            self,
            text = "FOOD MENU",
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

        #ENTRIES#

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
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #BUTTONS#

        #Search button
        self.buttonSearch = tk.Button(
            self,
            text = "SEARCH",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: self.searchFood(
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
            command = lambda: controller.show_frame(cmm.MainMenuClient)
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

        #TREEVIEW#

        #Food menu treeview
        self.tree = tk.ttk.Treeview(
            self,
            style = "Custom.Treeview",
            selectmode = "browse",
            columns = (
                "Kit Name",
                "Price",
                "Size"
            )
        )
        #Column 1 contains the Kit ID
        self.tree.heading(
            "#0",
            text = "Item Code"
        )
        #Column 2 contains the Kit Name
        self.tree.heading(
            "#1",
            text = "Kit Name"
        )
        #Column 3 contains the Kit Price
        self.tree.heading(
            "#2",
            text = "Price"
        )
        #Column 4 contains the Kit Size
        self.tree.heading(
            "#3",
            text = "Size"
        )
        #Adjust the width of the columns to decrease the overall size of the treeview,
        #Significantly trimming down on the size of the window
        self.tree.column(
            "#0",
            minwidth = 70,
            width = 70
        )
        self.tree.column(
            "#1",
            minwidth = 150,
            width = 150
        )
        self.tree.column(
            "#2",
            minwidth = 70,
            width = 70
        )
        self.tree.column(
            "#3",
            minwidth = 50,
            width = 50
        )
        self.tree.grid(
            row = 3,
            columnspan = 4,
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
            row = 3,
            columnspan = 4,
            sticky = "nse",
            pady = 10,
            padx = 10
        )
        #Set vertical movement of scrollbar to manipulate vertical scrolling of the treeview
        self.tree.configure(yscrollcommand = self.scroll.set)

    #Method for populating the treeview with the contents of the Kit table
    def updateTable(
        self,
        table 
    ):
        table.delete(*table.get_children()) #Clear contents of treeview
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        fetch = """SELECT * FROM KIT""" #Fetch everything from the Kit table, everything.
        cursor.execute(fetch)
        i = 0 #init iterator
        for row in cursor: #iterate through contents of cursor
            table.insert( #insert currently selected row into treeview
                "",
                "end",
                text = str(i),
                values = (row[1], row[2], row[3])
            )
            i += 1 #increase counter
        connection.close() #close connection

    #Method for searching through the Kit Table
    def searchFood(
        self,
        term,
        table
    ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        #SQL statement that fetches every record in kit that contains the search term
        search = """SELECT * FROM KIT WHERE (?) IN (kit_id, kit_name, price, size)"""
        cursor.execute(search, (term,)) #Execute search
        i = 0 #init iterator
        for row in cursor.fetchall(): #iterate through contents of cursor
            table.insert( #insert currectly selected row in cursor into treeview
                "",
                "end",
                text = str(i),
                values = (row[1], row[2], row[3])
            )
            i += 1 #increase counter
        connection.close() #close connection
        cursor.close() #close cursor