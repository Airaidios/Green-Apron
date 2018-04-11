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

        #Styling 
        self.configure(background = "gray20")

        #Labels 

        #Menu Title Label 
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

        #Buttons 

        #Place order button
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

        #Edit order button 
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

        #View orders 
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

        #Delete button 
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
                self.entryDelete.get()
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

        #Entries 

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

    def deleteItem(
        self,
        oid
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        select = """SELECT order_id FROM ("ORDER") WHERE order_id = ?"""
        cursor.execute(
            select,
            (oid,)
        )
        if oid.isdecimal() == True:
            if cursor.fetchone():
                delete = """DELETE FROM ("ORDER") WHERE order_id = ?"""
                cursor.execute(
                    delete,
                    oid
                )
                connection.commit()
            else:
                pass 
        else:
            pass