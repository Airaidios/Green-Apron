#imports
import tkinter as tk
import sqlite3 as sql
import StaffStock as ss

#main class
class EditIngredient(tk.Frame):

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

        #Styling
        self.configure(bg = "gray20")

        #Populate allergen dropdown
        self.allergen_choice = tk.StringVar(controller)
        self.allergens = {
            "None",
            "Eggs",
            "Fish",
            "Peanuts",
            "Shellfish",
            "Soy",
            "Tree Nuts",
            "Wheat"
        }
        self.allergen_choice.set("None")

        #Populate type dropdown
        self.type_choice = tk.StringVar(controller)
        self.types = {
            "Other",
            "Meat",
            "Fruit",
            "Vegetable",
            "Nut",
            "Bread",
            "Pasta",
            "Fish"
        }
        self.type_choice.set("Other")

        #Labels

        #Title label
        self.label = tk.Label(
            self,
            text = "EDIT INGREDIENT",
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

        #Ingredient ID label
        self.labelID = tk.Label(
            self,
            text = "INGREDIENT ID",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelID.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Ingredient name label
        self.labelName = tk.Label(
            self,
            text = "INGREDIENT NAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelName.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Ingredient Quantity label
        self.labelQuant = tk.Label(
            self,
            text = "INGREDIENT QUANTITY",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelQuant.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Allergen label
        self.labelAllergen = tk.Label(
            self,
            text = "SELECT ALLERGEN",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelAllergen.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Type label
        self.labelType = tk.Label(
            self,
            text = "SELECT TYPE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelType.grid(
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Ingredient ID entry
        self.entryID = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white",
            width = 25
        )
        self.entryID.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Ingredient name entry
        self.entryName = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white",
            width = 25
        )
        self.entryName.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Ingredient quantity entry
        self.entryQuant = tk.Entry(
            self,
            bd = 2,
            bg = "gray30",
            fg = "white",
            width = 25
        )
        self.entryQuant.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdrowns

        #Allergen dropdown
        self.popAllergen = tk.OptionMenu(
            self,
            self.allergen_choice,
            *self.allergens
            )
        self.popAllergen.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
            )

        #Type dropdown
        self.popType = tk.OptionMenu(
            self,
            self.type_choice,
            *self.types
        )
        self.popType.grid(
            row = 5,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Save button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.addIngredient(
                self.entryName.get(),
                self.entryQuant.get(),
                self.allergen_choice.get(),
                self.type_choice.get(),
                self.entryID.get()
            )
        )
        self.buttonSave.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Return Button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(ss.StockPage)
        )
        self.buttonReturn.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for updating ingredient information
    def addIngredient(
        self,
        name,
        quant,
        allergen,
        type_choice,
        iid
    ):
        #Create tuples that will be used with the SQL statement, containing
        #the new data as well as the ingredient ID
        Name = (name, iid) 
        Quant = (quant, iid)
        Aller = (allergen, iid)
        Type = (type_choice, iid)
        connection = sql.connect("ga.db") #connect to db
        cursor = connection.cursor() #init cursor
        #Update ing_name record in Ingredient table with new data
        addName = """UPDATE INGREDIENT SET (ing_name) = (?) WHERE ing_id = ?"""
        #Update quantity record in Ingredient table with new data
        addQuant = """UPDATE INGREDIENT SET (ing_quant) = (?) WHERE ing_id = ?"""
        #Update allergy record in Ingredient table with new data
        addAller = """UPDATE INGREDIENT SET (allergy) = (?) WHERE ing_id = ?"""
        #Update type record in Ingredient table with new data
        addType = """UPDATE INGREDIENT SET (type) = (?) WHERE ing_id = ?"""
        if not (len(name)) == 0: #Ingredient name presence check
            if name.isalpha() == True: #Ingredient name type check
                cursor.execute(addName, Name) #execute update
        if not (len(quant)) == 0: #quantity presence check
            if quant.isdecimal() == True: #quantity type check
                cursor.execute(addQuant, Quant) #execute update
        cursor.execute(addAller, Aller) #execute update
        cursor.execute(addType, Type) #execute update
        connection.commit() #save changes
        cursor.close() #close cursor
        connection.close() #close connection
