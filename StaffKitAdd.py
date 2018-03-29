#imports
import tkinter as tk
import sqlite3 as sql
import StaffKitMenu as skm

#main class
class AddKit(tk.Frame):

    #initialise method
    def __init__(
        self,
        parent,
        controller
    ):

        tk.Frame.__init__(
            self,
            parent
        )

        #Styling
        self.configure(background = "gray20")

        #Dictionary for size dropdown
        self.size = tk.StringVar(controller)
        self.sizes = {
            "S",
            "M",
            "L"
        }
        self.size.set("S")

        #labels

        #title
        self.label = tk.Label(
            self,
            text = "ADD KIT",
            font = controller.LARGE_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
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
            row = 1,
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
            row = 2,
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
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Name entry
        self.nameEntry = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.nameEntry.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Price entry
        self.priceEntry = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.priceEntry.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdown

        #size dropdown
        self.popSize = tk.OptionMenu(
            self,
            self.size,
            *self.sizes
        )
        self.popSize.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Save button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.addItem(
                self.nameEntry.get(),
                self.size.get(),
                self.priceEntry.get()
            )
        )
        self.buttonSave.grid(
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
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: controller.show_frame(skm.StaffKitsMenu)
        )
        self.buttonReturn.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    def addItem(
        self,
        name,
        size,
        price
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        addKit = """INSERT INTO KIT (kit_name) VALUES (?)"""
        addSize = """INSERT INTO KIT (size) VALUES (?)"""
        addPrice = """INSERT INTO KIT (price) VALUES (?)"""
        if not (len(name)) == 0:
            if name.isalpha() == True:
                cursor.execute(addKit, name)
            else:
                pass 
        else:
            pass 
        cursor.execute(addSize, size)
        if not (len(price)) == 0:
            if price.isdecimal() == True:
                cursor.execute(addPrice, price)
            else:
                pass 
        else:
             pass 
        connection.commit()
        cursor.close()
