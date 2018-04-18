#imports
import tkinter as tk 
import sqlite3 as sql 
import ClientOrderMenu as com 

#main class 
class ClientOrderEdit(tk.Frame):

    #initialise method 
    def __init__(
        self,
        parent,
        controller
    ):

        #initialise frame
        tk.Frame.__init__(
            self,
            parent
        )

        #styling
        self.configure(bg = "gray20")

        #LABELS#

        #Menu title label
        self.labelTitle = tk.Label(
            self,
            text = "EDIT ORDER",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Order ID entry label
        self.labelOrder = tk.Label(
            self,
            text = "ORDER ID",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelOrder.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Kit ID entry label
        self.labelKit = tk.Label(
            self,
            text = "KIT ID",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelKit.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #ENTRIES#

        #Order ID entry
        self.entryOrder = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.entryOrder.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
        
        #Kit ID entry
        self.entryKit = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.entryKit.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )


        #BUTTONS#

        #Return button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            font = controller.SMALL_FONT,
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(com.ClientOrderMenu)
        )
        self.buttonReturn.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Save button
        self.buttonSave = tk.Button(
            self,
            text = "CONFIRM",
            fg = "#44D276",
            bg = "gray10",
            font = controller.SMALL_FONT,
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.updateOrder(
                self.entryKit.get(),
                self.entryOrder.get(),
                controller.accountID
            )
        )
        self.buttonSave.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for updating order
    def updateOrder(
        self,
        kid,
        oid,
        aid
    ):
        Kit = (kid, oid, aid) #Create a tuple that contains the new data, order_id, and account ID
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        #SQL Statement that updates the record in the DB with the entered ID with the new data, but only
        #if the record belongs to the user
        update = """UPDATE "ORDER" SET (kit_id) = (?) WHERE (order_id) = ? AND (client_id) = ?"""
        if not kid == None: #Kit ID presence check
            if kid.isdecimal() == True: #Kit ID type check
                cursor.execute(update, Kit) #Execute update
        connection.commit() #Save changes to DB
        cursor.close() #Close connection