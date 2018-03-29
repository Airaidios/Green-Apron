#imports
import tkinter as tk
import StaffFood as sf
import StaffRecipeAdd as sra
import StaffRecipeEdit as sre
import StaffRecipeView as srv
import sqlite3 as sql

#main class
class StaffRecipeMenu(tk.Frame):

    #initialise Method
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

        #Title
        label = tk.Label(
                            self,
                            text = "RECIPE MENU",
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


        #buttons

        #Add kits
        addButton = tk.Button(
                                self,
                                text = "ADD RECIPE",
                                fg = "#44D276",
                                bg = "gray10",
                                activeforeground = "white",
                                activebackground = "#44D276",
                                font = controller.SMALL_FONT,
                                width = 25,
                                command = lambda: controller.show_frame(sra.AddRecipe)
                                )
        addButton.grid(
                                row = 1,
                                column = 0,
                                columnspan = 2,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Edit kits
        editButton = tk.Button(
                                self,
                                text = "EDIT RECIPE",
                                fg = "#44D276",
                                bg = "gray10",
                                activeforeground = "white",
                                activebackground = "#44D276",
                                font = controller.SMALL_FONT,
                                width = 25,
                                command = lambda: controller.show_frame(sre.StaffRecipeEdit)
                                )
        editButton.grid(
                                row = 2,
                                column = 0,
                                columnspan = 2,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #View kits
        viewButton = tk.Button(
                                self,
                                text = "VIEW RECIPES",
                                fg = "#44D276",
                                bg = "gray10",
                                activeforeground = "white",
                                activebackground = "#44D276",
                                font = controller.SMALL_FONT,
                                width = 25,
                                command = lambda: controller.show_frame(srv.StaffRecipeView)
                                )
        viewButton.grid(
                                row = 3,
                                column = 0,
                                columnspan = 2,
                                sticky = "ns",
                                pady = 10,
                                padx = 10
                                )

        #Delete kits
        deleteButton = tk.Button(
                                    self,
                                    text = "DELETE RECIPE",
                                    fg = "#44D276",
                                    bg = "gray10",
                                    activeforeground = "white",
                                    activebackground = "#44D276",
                                    font = controller.SMALL_FONT,
                                    width = 25,
                                    #command = lambda: self.deleteItem(idEntry.get())
                                    )
        deleteButton.grid(
                                    row = 4,
                                    column = 1,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #Return button
        returnButton = tk.Button(
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
        returnButton.grid(
                                    row = 5,
                                    column = 0,
                                    columnspan = 2,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #Entries

        #Id Entry
        idEntry = tk.Entry(
                            self,
                            fg = "white",
                            bg = "gray30",
                            bd = 2,
                            width = 25
                            )
        idEntry.grid(
                            row = 4,
                            column = 0,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

    #Delete recipe
    def deleteItem(
                    self,
                    rid
                    ):
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        select = """SELECT rec_id FROM RECIPE WHERE rec_id = ?"""
        cursor.execute(
                        select,
                        (rid,)
                        )
        if rid.isdecimal() == True:
            if cursor.fetchone():
                delete = """DELETE FROM RECIPE WHERE rec_id = ?"""
                cursor.execute(
                                delete,
                                rid
                                )
                connection.commit()
            else:
                pass 
        else:
            pass