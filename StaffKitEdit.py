#imports
import tkinter as tk
import StaffKitMenu as skm
import sqlite3 as sql

#main class
class StaffKitEdit(tk.Frame):

    #initialise Method
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

        #Dictionary for size dropdown
        self.size = tk.StringVar(controller)
        self.sizes = {
            "S",
            "M",
            "L"
        }
        self.size.set("S")

        #labels

        #Title
        self.titleLabel = tk.Label(
            self,
            text = "EDIT KIT",
            fg = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.titleLabel.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #ID label
        self.idLabel = tk.Label(
            self,
            text = "KIT ID",
            fg = "white",
            bg = "gray20",
            activeforeground = "white",
            activebackground = "#44D276",
            font = controller.SMALL_FONT,
        )
        self.idLabel.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Name Label
        self.nameLabel = tk.Label(
            self,
            text = "KIT NAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.nameLabel.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Price label
        self.priceLabel = tk.Label(
            self,
            text = "KIT PRICE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.priceLabel.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Size label
        self.sizeLabel = tk.Label(
            self,
            text = "KIT SIZE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.sizeLabel.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #ID entry
        self.idEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.idEntry.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Name entry
        self.nameEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.nameEntry.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        self.priceEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.priceEntry.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdowns

        #Size dropdown
        self.popSize = tk.OptionMenu(
            self,
            self.size,
            *self.sizes
        )
        self.popSize.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #buttons

        #Return buttons
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(skm.StaffKitsMenu)
        )
        self.buttonReturn.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #save button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.updateItem(
                self.nameEntry.get(),
                self.priceEntry.get(),
                self.size.get(),
                self.idEntry.get()
            )
        )
        self.buttonSave.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    def updateItem(
        self,
        name,
        price,
        size,
        kid
    ):
        Name = (name, kid)
        Price = (price, kid) 
        Size = (size, kid)
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        #I split the update statements so I can ignore empty fields
        addName = """UPDATE KIT SET (kit_name) = (?) WHERE kit_id = ?"""
        addPrice = """UPDATE KIT SET (price) = (?) WHERE kit_id = ?"""
        addSize = """UPDATE KIT SET (size) = (?) WHERE kit_id = ?"""
        #update Name
        if not (len(name)) == 0: #Presence check
            if not name.isalpha() == False: #Type check
                cursor.execute(addName, Name)
            else:
                pass 
        else:
            pass
        #Update price
        if not (len(price)) == 0:
            if not price.isdecimal() == False:
                cursor.execute(addPrice, Price)
            else:
                pass 
        else:
            pass
        #I don't need to validate this as it can only be taken from a set list of options
        cursor.execute(addSize, Size)
        connection.commit()
        cursor.close()
