#imports
import tkinter as tk
from tkinter.ttk import *
import sqlite3 as sql
import StaffOrder as so

#main class
class ActiveOrder(tk.Frame):

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


        #background colour
        self.configure(bg = "gray20")

        #define a custom ttk style to use with the treeview, could be moved to Main and inherited
        #But this current implementation works just fine
        style = tk.ttk.Style()
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nsew'}),
            ("Custom.Treeheading.border", {'sticky':'nsew', 'children': [
                ("Custom.Treeheading.padding", {'sticky':'nsew', 'children': [
                    ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
                    ("Custom.Treeheading.text", {'sticky':'we'})
                ]})
            ]}),
        ])
        style.configure("Custom.Treeview.Heading",
            background="gray15", foreground="white", relief="flat")
        style.configure("Treeview",
            background = "gray30", foreground = "white", fieldbackground = "gray30")
        style.map("Custom.Treeview.Heading",
            relief=[('active','groove'),('pressed','sunken')])

        #Labels

        #Menu title Label
        label = tk.Label(
                            self,
                            text = "ACTIVE ORDERS",
                            font = controller.LARGE_FONT,
                            fg = "white",
                            bg = "gray20"
                            )
        label.grid(
                            row = 0,
                            column = 2,
                            sticky = "ns",
                            pady = 10,
                            padx = 10
                            )

        #Buttons

        #back button
        buttonReturn = tk.Button(
                                    self,
                                    text = "RETURN",
                                    fg = "#44D276",
                                    bg = "gray10",
                                    activebackground = "#44D276",
                                    activeforeground = "white",
                                    width = 25,
                                    font = controller.SMALL_FONT,
                                    command = lambda: controller.show_frame(so.OrderPageStaff)
                                    )
        buttonReturn.grid(
                                row = 10,
                                column = 1,
                                sticky = "ns",
                                padx = 10,
                                pady = 10
                                )

        #Refresh table button
        buttonRefresh = tk.Button(
                                    self,
                                    text = "REFRESH",
                                    fg = "#44D276",
                                    bg = "gray10",
                                    activebackground = "#44D276",
                                    activeforeground = "white",
                                    width = 25,
                                    font = controller.SMALL_FONT,
                                    command = lambda: self.populateTable(self.tree)
                                    )
        buttonRefresh.grid(
                                    row = 10,
                                    column = 3,
                                    sticky = "ns",
                                    pady = 10,
                                    padx = 10
                                    )

        #Treeviews

        #active orders treeview, displays a readout of all records present in the order table.
        #Updated when "populateOrders" is called
        self.tree = tk.ttk.Treeview(
                                    self,
                                    style = "Custom.Treeview",
                                    columns  = (
                                                "Client ID",
                                                "Kit"
                                                )
                                    )
        self.tree.heading(
                                    "#0",
                                    text = "Order ID"
                                    )
        self.tree.heading(
                                    "#1",
                                    text = "Client ID"
                                    )
        self.tree.heading(
                                    "#2",
                                    text = "Kit ID"
                                    )
        self.tree.grid(
                                    row = 3,
                                    columnspan = 4,
                                    sticky = "ns"
                                    )

    #populate treeview with records from database
    def populateTable(
                        self,
                        table
                        ):
        table.delete(*table.get_children())
        connection = sql.connect("ga.db")
        cursor = connection.cursor()
        insert = """SELECT * FROM ("ORDER")"""
        cursor.execute(insert)
        i = 0
        for row in cursor:
            table.insert(
                            "",
                            "end",
                            text = str(i),
                            values = (row[1], row[2])
                            )
            i += 1
