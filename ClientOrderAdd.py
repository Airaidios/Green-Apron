#imports
import ClientOrderMenu as com 
import sqlite3 as sql 
import tkinter as tk 

#main class
class ClientOrderAdd(tk.Frame):

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
        self.configure(bg = "gray20")

        #LABELS#

        #Menu title label
        self.labelTitle = tk.Label(
            self,
            text = "PLACE ORDER",
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

        #Label to identify the adjacent entry for Kit ID
        self.labelKit = tk.Label(
            self,
            text = "KIT ID",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelKit.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )
        
        #ENTRIES#
        
        #Kit ID entry
        self.entryKit = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.entryKit.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #BUTTONS

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
            row = 2,
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
            command = lambda: self.saveOrder(
                self.entryKit.get(),
                controller.accountID
            )
        )
        self.buttonSave.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Add order to database
    def saveOrder(
        self,
        kid,
        aid
    ):
        KitAccount = (kid, aid) #Create a tuple that can be used with the SQL statement below
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init a cursor
        #SQL statement to insert a record into the Order table that contains the kit_id entered
        #and the client_id taken from the token
        #ORDER is in quotations as ORDER is already a SQL function, this would cause syntax errors
        #if the quotation marks were removed
        add = """INSERT INTO "ORDER" (kit_id, client_id) VALUES (?, ?)"""
        if not kid == None: #Kit ID presence check
            if kid.isdecimal() == True: #Kit ID type check
                cursor.execute(add, KitAccount) #Execute insert
        connection.commit() #Save changes to DB
        cursor.close() #Close cursor