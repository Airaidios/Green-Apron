#imports
import tkinter as tk
import StaffFood as sf
import StaffKitAdd as ska
import StaffKitEdit as ske
import StaffKitView as skv
import sqlite3 as sql

#main class
class StaffKitsMenu(tk.Frame):

    #Initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        #Initialise frames
        tk.Frame.__init__(
            self,
            parent
        )

        #Styling
        self.configure(bg = "gray20")

        #Labels

        #title
        self.label = tk.Label(
            self,
            text = "KIT MENU",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #buttons

        #Add kits
        self.addButton = tk.Button(
            self,
            text = "ADD KIT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(ska.AddKit)
        )
        self.addButton.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Edit kits
        self.editButton = tk.Button(
            self,
            text = "EDIT KIT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(ske.StaffKitEdit)
        )
        self.editButton.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #View kits
        self.viewButton = tk.Button(
            self,
            text = "VIEW KITS",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(skv.ViewKit)
        )
        self.viewButton.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Delete kits
        self.deleteButton = tk.Button(
            self,
            text = "DELETE KIT",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: self.deleteItem(self.idEntry.get())
        )
        self.deleteButton.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Return button
        self.returnButton = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
            width = 25,
            command = lambda: controller.show_frame(sf.MenuPageStaff)
        )
        self.returnButton.grid(
            row = 5,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Id Entry
        self.idEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.idEntry.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Delete item from the Kit table
    def deleteItem(
        self,
        kid
    ):
        connection = sql.connect("ga.db") #connect to db
        cursor = connection.cursor() #init cursor
        #fetch record with the entered Kit ID
        select = """SELECT kit_id FROM KIT WHERE kit_id = ?"""
        cursor.execute(select, (kid),) #execute fetch
        if kid.isdecimal() == True: #kit id presence check
            if cursor.fetchone(): #check if sql statement returned anything
                delete = """DELETE FROM KIT WHERE kit_id = ?""" #delete record from kit table
                cursor.execute(delete, kid) #execute delete
                connection.commit() #save changes
        connection.close() #close connection
        cursor.close() #close cursor