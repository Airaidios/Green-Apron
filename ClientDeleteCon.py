#imports
import tkinter as tk 
import sqlite3 as sql 
import ClientAccountMenu as cam 
import Login as l

#main class 
class ClientDeleteCon(tk.Frame):

    #Initialise method
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
            text = "CONFIRM DELETION",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Confirm text
        self.labelConfirm = tk.Label(
            self,
            text = "ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT? THIS CANNOT BE UNDONE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelConfirm.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Return button
        self.buttonBack = tk.Button(
            self,
            text = "CANCEL",
            fg = "#44D276",
            bg = "gray10",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(cam.ClientAccountMenu)
        )
        self.buttonBack.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Confirm button
        self.buttonConfirm = tk.Button(
            self,
            text = "CONFIRM",
            fg = "red",
            bg = "gray30",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: self.deleteAccount(controller.accountID, controller)
        )
        self.buttonConfirm.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    def deleteAccount(
        self,
        aid,
        controller
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        select = """SELECT client_id FROM CLIENT WHERE client_id = ?"""
        cursor.execute(
            select,
            (aid,)
        )
        if cursor.fetchone():
            delete = """DELETE FROM CLIENT WHERE client_id = ?"""
            cursor.execute(
                delete,
                (aid,)
            )
            connection.commit()
        else:
            pass
        controller.show_frame(l.Login)
        connection.comitt()
        cursor.close()


