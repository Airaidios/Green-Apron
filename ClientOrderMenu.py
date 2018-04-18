#imports
import tkinter as tk
import ClientMainMenu as cmm 
import ClientOrderAdd as coa 
import ClientOrderEdit as coe
import ClientOrderView as cov 
import sqlite3 as sql

#main class
class ClientOrderMenu(tk.Frame): 

    #Initialise method 
    def __init__(
        self,
        parent,
        controller
    ):

        #Initialise frame 
        tk.Frame.__init__(
            self,
            parent
        )

        #Styling - set background colour
        self.configure(background = "gray20")

        #LABELS#

        #Menu title label 
        self.labelTitle = tk.Label(
            self,
            text = "ORDER MANAGEMENT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20",
            width = 25,
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #BUTTONS#

        #Button that brings user to Add Order menu
        self.buttonAdd = tk.Button(
            self,
            text = "PLACE ORDER",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(coa.ClientOrderAdd)
        )
        self.buttonAdd.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Button to bring user Edit Order menu 
        self.buttonEdit = tk.Button(
            self,
            text = "EDIT ORDER",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(coe.ClientOrderEdit)
        )
        self.buttonEdit.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Button to bring user to a table containing their placed orders
        self.buttonView = tk.Button(
            self,
            text = "VIEW ORDERS",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(cov.ClientOrderView)
        )
        self.buttonView.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Button to delete order with ID entered in adjacent entry - but only
        #If the client_id of that order is equal to the contents of the 
        #account ID token
        self.buttonDelete = tk.Button(
            self,
            text = "CANCEL ORDER",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44d276",
            width = 25,
            command = lambda: self.deleteItem(
                self.entryDelete.get(),
                controller.accountID
            )
        )
        self.buttonDelete.grid(
            row = 4,
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
            activebackground = "#44d276",
            width = 25,
            command = lambda: controller.show_frame(cmm.MainMenuClient)
        )
        self.buttonReturn.grid(
            row = 5,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #ENTRIES#

        #Delete ID entry 
        self.entryDelete = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.entryDelete.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for deleting a record in the Order table if the client_id in that record
    #is equal to the contents of the accountID token
    def deleteItem(
        self,
        oid,
        aid
    ):
        connection = sql.connect("ga.db") #Establish connection to central database
        cursor = connection.cursor() #Initialise a cursor
        #SQL statement for fetching the entered record if it belongs to the user
        select = """SELECT order_id FROM ("ORDER") WHERE order_id = ? AND client_id = ?"""
        cursor.execute( #Execute SQL statement
            select,
            (oid, aid)
        )
        if oid.isdecimal() == True: #Order ID type check
            if cursor.fetchone(): #Check if the cursor comes up empty (i.e. If the entered ID exists in the table)
                #SQL statement for deleting relevant record
                delete = """DELETE FROM ("ORDER") WHERE order_id = ? AND client_id"""
                cursor.execute( #Execute deletion
                    delete,
                    (oid, aid)
                )
        connection.commit() #Save changes to database
        cursor.close() #Close connection