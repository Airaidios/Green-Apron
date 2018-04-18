#imports
import tkinter as tk
import sqlite3 as sql
import StaffStock as ss

#main class
class AddIngredient(tk.Frame):

    #initialise method
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
        self.configure(background = "gray20")

        #create a string that will be used to populate
        #a dropdown menu
        #Allergy dropdown menu
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
        #set the default value for the dropdown to "none"
        self.allergen_choice.set("None")

        #Food type dropdown menu
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
            text = "ADD INGREDIENT",
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

        #Ingredient Name entry Label
        self.labelName = tk.Label(
            self,
            text = "INGREDIENT NAME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.labelName.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Allergen dropdown label
        self.labelAllergen = tk.Label(
            self,
            text = "SELECT ALLERGEN",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
            width = 25
        )
        self.labelAllergen.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Type dropdown label
        self.labelType = tk.Label(
            self,
            text = "SELECT TYPE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
            width = 25
        )
        self.labelType.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #recipe ID label
        self.labelRecipeID = tk.Label(
            self,
            text = "RECIPE ID",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT,
            width = 25
        )
        self.labelRecipeID.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Entries

        #Ingredient name entry
        self.entryName = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2,
            width = 25
        )
        self.entryName.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        self.entryRecipeID = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2,
            width = 25
        )
        self.entryRecipeID.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdowns

        #Allergy information dropdown
        self.popAllergen = tk.OptionMenu(
            self,
            self.allergen_choice,
            *self.allergens,
        )
        self.popAllergen.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Food type dropdown
        self.popType = tk.OptionMenu(
            self,
            self.type_choice,
            *self.types
        )
        self.popType.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Add details to database button
        self.buttonSave = tk.Button(
            self,
            text = "SAVE",
            fg = "#44D276",
            bg = "gray10",
            activebackground = "#44D276",
            activeforeground = "white",
            width = 25,
            font = controller.SMALL_FONT,
            command = lambda: self.addIngredient(
                self.entryName.get(),
                self.allergen_choice.get(),
                self.type_choice.get(),
                self.entryRecipeID.get()
            )
        )
        self.buttonSave.grid(
            row = 5,
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
            command = lambda: controller.show_frame(ss.StockPage)
        )
        self.buttonReturn.grid(
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for adding ingredient details to the database, called by buttonSave
    #Integrated validation
    def addIngredient(
        self,
        name,
        allergen,
        type_choice,
        rid
    ):
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #init cursor
        Data = (name, allergen, type_choice, rid)
        #Insert new record with inputted data into Ingredient table
        addData = """INSERT INTO INGREDIENT (ing_name, allergy, type, rec_id) VALUES (?, ?, ?, ?)"""
        if not (len(name)) == 0: #Ingredient name presence check - different method, same result
            if name.isalpha() == True: #Ingredient name type check
                cursor.execute(addData, Data) #Execute insert
        connection.commit() #Close connection
        cursor.close() #Close cursor
