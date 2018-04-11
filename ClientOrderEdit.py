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

        #Labels

        #Title label
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

        #Order label
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

        #Kit label
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

        #Entries

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
                self.entryOrder.get()
            )
        )
        self.buttonSave.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Update order
    def updateOrder(
        self,
        kid,
        oid
    ):
        Kit = (kid, oid)
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        update = """UPDATE "ORDER" SET (kit_id) = (?) WHERE (order_id) = ?"""
        if not kid == None:
            if kid.isdecimal() == True:
                cursor.execute(update, Kit)
            else:
                pass 
        else:
            pass 
        connection.commit()
        cursor.close()