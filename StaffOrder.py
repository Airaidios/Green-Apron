#Imports
import tkinter as tk
import sqlite3 as sql
import StaffOrdersView as sov
import StaffMainMenu as smm

#Main class
class OrderPageStaff(tk.Frame):

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

        #Styling, sets background to a light gray
        self.configure(background = "gray20")

        #Labels

        #Menu title label
        self.label = tk.Label(
            self,
            text = "ORDER MANAGEMENT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20",
            width = 25
        )
        self.label.grid(
            row = 0,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Order ID entry, user enters the ID of the order they want to "complete" (delete),
        #Then presses the "delete order" button to remove the relevant record
        self.entryID = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2,
            width = 25,
            justify = "center"
        )
        self.entryID.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Delete order button
        self.buttonComplete = tk.Button(
            self,
            text = "COMPLETE ORDER",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.completeOrder(self.entryID.get())
        )
        self.buttonComplete.grid(
            row = 2,
            column = 2,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Active orders menu button, brings user to a treeview where they can view the
        #contents of the orders table
        self.buttonActiveOrders = tk.Button(
            self,
            text = "VIEW ACTIVE ORDERS",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(sov.ActiveOrder)
        )
        self.buttonActiveOrders.grid(
            row = 1,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Main menu button, brings user back to main menu
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(smm.MainMenuStaff)
        )
        self.buttonReturn.grid(
            row = 5,
            column = 1,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for deleting an order, input validation incorporated into it
    #Will check whether the entered is an integer and whether or not it
    #exists within the order table
    def completeOrder(
        self,
        oid,
    ):
        #Establish connection to central database
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        #Statement for checking whether the entered ID exists
        select = """SELECT order_id FROM ("ORDER") WHERE order_id = ?"""
        cursor.execute(
            select,
            (oid,)
        )
        if oid.isdecimal() == True:
            if cursor.fetchone():
                #Statement for deleting the relevant record
                delete = """DELETE FROM "ORDER" WHERE order_id = ?"""
                cursor.execute(
                    delete,
                    oid
                )
                #"Save changes"
                connection.commit()
        cursor.close()
        connection.close()