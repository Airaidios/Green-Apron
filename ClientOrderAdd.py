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

        #styling
        self.configure(bg = "gray20")

        #Labels

        #Title label
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

        #Kit label
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
        
        #Entries
        
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

        #Buttons

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
        KitAccount = (kid, aid)
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        add = """INSERT INTO "ORDER" (kit_id, client_id) VALUES (?, ?)"""
        if not kid == None:
            if kid.isdecimal() == True:
                cursor.execute(add, KitAccount)
            else:
                pass
        else:
            pass 
        connection.commit()
        cursor.close()