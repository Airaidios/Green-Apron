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
        label = tk.Label(
                            self,
                            text = "EDIT RECIPE",
                            fg = "white",
                            bg = "gray20",
                            font = controller.LARGE_FONT
                            )
        label.grid(
                            row = 0,
                            column = 0,
                            columnspan = 2,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #ID label
        idLabel = tk.Label(
                            self,
                            text = "RECIPE ID",
                            fg = "white",
                            bg = "gray20",
                            activeforeground = "white",
                            activebackground = "#44D276",
                            font = controller.SMALL_FONT,
                            )
        idLabel.grid(
                            row = 1,
                            column = 0,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Name Label
        nameLabel = tk.Label(
                            self,
                            text = "RECIPE NAME",
                            font = controller.SMALL_FONT,
                            fg = "white",
                            bg = "gray20"
                            )
        nameLabel.grid(
                            row = 2,
                            column = 0,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Serving label
        servingLabel = tk.Label(
                            self,
                            text = "RECIPE SERVINGS",
                            font = controller.SMALL_FONT,
                            fg = "white",
                            bg = "gray20"
                            )
        servingLabel.grid(
                            row = 3,
                            column = 0,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Prep label
        prepLabel = tk.Label(
                                self,
                                text = "PREP TIME",
                                font = controller.SMALL_FONT,
                                fg = "white",
                                bg = "gray20"
                                )
        prepLabel.grid(
                                row = 4,
                                column = 0,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Culture Label
        cultureLabel = tk.Label(
                                self,
                                text = "CULTURE",
                                font = controller.SMALL_FONT,
                                fg = "white",
                                bg = "gray20"
                                )
        cultureLabel.grid(
                                row = 5,
                                column = 0,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Entries

        #ID entry
        idEntry = tk.Entry(
                            self,
                            fg = "white",
                            bg = "gray30",
                            bd = 2,
                            width = 25
                            )
        idEntry.grid(
                            row = 1,
                            column = 1,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Name entry
        nameEntry = tk.Entry(
                                self,
                                fg = "white",
                                bg = "gray30",
                                bd = 2,
                                width = 25
                                )
        nameEntry.grid(
                                row = 2,
                                column = 1,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Recipe entry
        recipeEntry = tk.Entry(
                                self,
                                fg = "white",
                                bg = "gray30",
                                bd = 2,
                                width = 25
                                )
        recipeEntry.grid(
                                row = 3,
                                column = 1,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Servings entry
        servingsEntry = tk.Entry(
                                self,
                                fg = "white",
                                bg = "gray30",
                                bd = 2,
                                width = 25
                                )
        servingsEntry.grid(
                            row = 4,
                            column = 1,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Dropdowns

        #Culture dropdown
        popCulture = tk.OptionMenu(
                                    self,
                                    self.culture,
                                    *self.cultures
                                    )
        popCulture.grid(
                                    row = 5,
                                    column = 1,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #buttons

        #Return buttons
        buttonReturn = tk.Button(
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
        buttonReturn.grid(
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
                                #command = lambda: self.updateItem(
                                #                                   nameEntry.get(),
                                #                                   priceEntry.get(),
                                #                                   recipeEntry.get(),
                                #                                   self.size.get()
                                #                                   idEntry.get()
                                #                                    )
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