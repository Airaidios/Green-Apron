#imports
import tkinter as tk
import sqlite3 as sql
import StaffRecipeMenu as srm

#main class
class AddRecipe(tk.Frame):

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

        #Dictionary for Dropdown
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

        #Labels

        #Title
        self.label = tk.Label(
            self,
            text = "ADD RECIPE",
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
            text = "RECIPE NAME",
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

        #Culture Label
        self.cultureLabel = tk.Label(
            self,
            text = "RECIPE CULTURE",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.cultureLabel.grid(
            row = 2,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Servings label
        self.servingsLabel = tk.Label(
            self,
            text = "SERVINGS",
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.servingsLabel.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Prep time label
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

        #Entries

        #Name Entry
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

        #Servings entry
        self.servingsEntry = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.servingsEntry.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Prep Time entry
        self.prepEntry = tk.Entry(
            self,
            bg = "gray30",
            fg = "white",
            bd = 2
        )
        self.prepEntry.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Buttons

        #Save Button
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
                self.culture.get(),
                self.servingsEntry.get(),
                self.prepEntry.get()
            )
        )
        self.buttonSave.grid(
            row = 5,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Return Button
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
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Dropdowns

        #Culture Dropdown
        self.popCulture = tk.OptionMenu(
            self,
            self.culture,
            *self.cultures
        )
        self.popCulture.grid(
            row = 2,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Method for adding record to table
    def addItem(
        self,
        name,
        culture,
        servings,
        prep
    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        addRec = """INSERT INTO RECIPE (rec_name) VALUES (?)"""
        addCult = """INSERT INTO RECIPE (culture) VALUES (?)"""
        addServe = """INSERT INTO RECIPE (servings) VALUES (?)"""
        addPrep = """INSERT INTO RECIPE (prep) VALUES (?)"""
        if not (len(name)) == 0:
            if name.isalpha() == True:
                    cursor.execute(addRec, name)
            else:
                pass 
        else:
            pass 
        cursor.execute(addCult, culture)
        if not (len(servings)) == 0:
            if servings.isdecimal() == True:
                cursor.execute(addServe, servings)
            else:
                pass 
        else:
            pass 
        if not (len(prep)) == 0:
            if prep.isdecimal() == True:
                cursor.execute(addPrep, prep)
        connection.commit()
        cursor.close()
