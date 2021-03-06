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

    #add entered data into a new record in kit table
    def addItem(
        self,
        name,
        size,
        price
    ):
        connection = sql.connect("ga.db") #connect to db
        cursor = connection.cursor() #init cursor
        Data = (name, size, price) #create a tuple with new data
        #Insert entered data into table
        addKit = """INSERT INTO KIT (kit_name, size, price) VALUES (?, ?, ?)"""
        if not (len(name)) == 0 and name.isalpha() == True: #name presence and type check
                if not (len(price)) == 0 and price.isdecimal() == True: #price presence and type check
                    cursor.execute(addKit, Data) #execute insert
                    connection.commit() #save changes
        cursor.close() #close cursor
        connection.close() #close connection
