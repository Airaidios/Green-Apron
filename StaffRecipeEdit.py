#imports
import tkinter as tk
import StaffRecipeMenu as srm
import sqlite3 as sql

#main class
class StaffRecipeEdit(tk.Frame):

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

        #Dictionary for dropdown
        self.culture = tk.StringVar(controller)
        self.cultures = {
            "None",
            "American",
            "British",
            "Chinese",
            "English",
            "European",
            "Indian",
            "Italian",
            "Japanese",
            "Turkish",
            "Mexican",
        }
        self.culture.set("None")

        #labels

        #Title
        self.label = tk.Label(
            self,
            text = "EDIT RECIPE",
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

        #ID label
        self.idLabel = tk.Label(
            self,
            text = "RECIPE ID",
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
            text = "RECIPE NAME",
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

        #Serving label
        self.servingLabel = tk.Label(
            self,
            text = "RECIPE SERVINGS",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.servingLabel.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Prep label
        self.prepLabel = tk.Label(
            self,
            text = "PREP TIME",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.prepLabel.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Culture Label
        self.cultureLabel = tk.Label(
            self,
            text = "CULTURE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.cultureLabel.grid(
            row = 5,
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

        #Recipe entry
        self.recipeEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.recipeEntry.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Servings entry
        self.servingsEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray30",
            bd = 2,
            width = 25
        )
        self.servingsEntry.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Prep entry
        self.prepEntry = tk.Entry(
            self,
            fg = "white",
            bg = "gray20",
            bd = 2,
            width = 25
        )
        self.prepEntry.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdowns

        #Culture dropdown
        self.popCulture = tk.OptionMenu(
            self,
            self.culture,
            *self.cultures
        )
        self.popCulture.grid(
            row = 5,
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
            command = lambda: controller.show_frame(srm.StaffRecipeMenu)
        )
        self.buttonReturn.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #save button
        buttonSave = tk.Button(
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
                self.culture.get(),
                self.servingsEntry.get(),
                self.prepEntry.get(),
                self.idEntry.get()
            )
        )
        buttonSave.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    def updateItem(
        self,
        name,
        culture,
        servings,
        prep,
        rid
    ):
        Name = (name, rid)
        Cult = (culture, rid) 
        Serve = (servings, rid)
        Prep = (prep, rid)
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        addName = """UPDATE RECIPE SET (rec_name) = (?) WHERE (rec_id) = ?"""
        addCult = """UPDATE RECIPE SET (culture) = (?) WHERE (rec_id) = ?"""
        addServe = """UPDATE RECIPE SET (servings) = (?) WHERE (rec_id) = ?"""
        addPrep = """UPDATE RECIPE SET (prep_time) = (?) WHERE (rec_id) = ?"""
        if not name == None:
            if not name.isalpha() == True:
                cursor.execute(addName, Name)
        if not culture == None:
            if not culture.isalpha() == True:
                cursor.execute(addCult, Cult)
        if not servings == None:
            if not servings.isdecimal() == True:
                cursor.execute(addServe, Serve)
        if not prep == None:
            if not prep.isdecimal() == True:
                cursor.execute(addPrep, Prep)
        connection.commit()
        cursor.close()