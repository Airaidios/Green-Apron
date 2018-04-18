#imports
import tkinter as tk 
import sqlite3 as sql 
import ClientAccountMenu as cam

#main class
class ClientAccountView(tk.Frame):

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
        self.configure(bg = "gray20")

        #LABELS#

        #Title label
        self.labelTitle = tk.Label(
            self,
            text = "VIEW ACCOUNT DETAILS",
            fg  = "white",
            bg = "gray20",
            font = controller.LARGE_FONT
        )
        self.labelTitle.grid(
            row = 0,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #username
        self.labelusername = tk.Label(
            self,
            text = "username",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelusername.grid(
            row = 1,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Address
        self.labelAddress = tk.Label(
            self,
            text = "ADDRESS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelAddress.grid(
            row = 3,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Package
        self.labelPackage = tk.Label(
            self,
            text = "PACKAGE",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelPackage.grid(
            row = 4,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Diet requirements
        self.labelDiet = tk.Label(
            self,
            text = "DIET REQUIREMENTS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelDiet.grid(
            row = 5,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Email
        self.labelMail = tk.Label(
            self,
            text = "EMAIL ADDRESS",
            fg = "white",
            bg = "gray20",
            font = controller.SMALL_FONT
        )
        self.labelMail.grid(
            row = 6,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #DISPLAY LABELS#
        #These are not intialised with text, instead, the text is added later when the user clicks the "Refresh" button
        #I used labels to display the account details because a client user will only be viewing the details of one account, theirs

        #username display
        self.displayusername = tk.Label(
            self,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.displayusername.grid(
            row = 1,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Address display
        self.displayAddress = tk.Label(
            self,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20",
        )
        self.displayAddress.grid(
            row = 3,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Package display
        self.displayPackage = tk.Label(
            self,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayPackage.grid(
            row = 4,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Diet display
        self.displayDiet = tk.Label(
            self,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayDiet.grid(
            row = 5, 
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Mail display
        self.displayMail = tk.Label(
            self,
            font = controller.SMALL_FONT,
            fg = "white",
            bg = "gray20"
        )
        self.displayMail.grid(
            row = 6,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #BUTTONS#

        #Return button
        self.buttonReturn = tk.Button(
            self,
            text = "RETURN",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: controller.show_frame(cam.ClientAccountMenu)
        )
        self.buttonReturn.grid(
            row = 7,
            column = 0,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

        #Refresh button
        self.buttonRefresh = tk.Button(
            self,
            text = "REFRESH",
            font = controller.SMALL_FONT,
            fg = "#44D276",
            bg = "gray10",
            activeforeground = "white",
            activebackground = "#44D276",
            width = 25,
            command = lambda: self.updateDetails(
                self.displayusername,
                self.displayAddress,
                self.displayPackage,
                self.displayDiet,
                self.displayMail,
                controller.accountID
            )
        )
        self.buttonRefresh.grid(
            row = 7,
            column = 1,
            sticky = "ns",
            pady = 10,
            padx = 10
        )

    #Refresh account details and update the contents of the stringVars (the text of the display labels)     
    def updateDetails(
        self,
        usernamedisplay,
        addressdisplay,
        packagedisplay,
        dietdisplay,
        maildisplay,
        aid
    ):
        connection = sql.connect("ga.db") #Connect to DB
        cursor = connection.cursor() #Init cursor
        #Fetch username from account record belonging to user
        fetchUsername = """SELECT username FROM CLIENT WHERE client_id = ?"""
        #Fetch address from account record belonging to user
        fetchAddress = """SELECT address FROM CLIENT WHERE client_id = ?"""
        #Fetch package from account record belonging to user
        fetchPackage = """SELECT package FROM CLIENT WHERE client_id = ?"""
        #Fetch dietary_requirements from account record belonging to user
        fetchDiet = """SELECT diet_req FROM CLIENT WHERE client_id = ?"""
        #Fetch email address from account record belonging to user
        fetchMail = """SELECT email FROM CLIENT WHERE client_id = ?"""
        cursor.execute(fetchUsername, (aid,)) #Execute fetch
        Username = str(cursor.fetchone()[0]) #Update stringVar
        cursor.execute(fetchAddress, (aid,)) #Execute fetch
        Address = str(cursor.fetchone()[0]) #Update stringVar
        cursor.execute(fetchPackage, (aid,)) #Execute fetch
        Package = str(cursor.fetchone()[0]) #Update stringVar
        cursor.execute(fetchDiet, (aid,)) #Execute fetch
        Diet = str(cursor.fetchone()[0]) #Update stringVar
        cursor.execute(fetchMail, (aid,)) #Execute fetch
        Mail = str(cursor.fetchone()[0]) #Update stringVar
        usernamedisplay.configure(text = Username) #Update display labels with new data
        addressdisplay.configure(text = Address)
        packagedisplay.configure(text = Package)
        dietdisplay.configure(text = Diet)
        maildisplay.configure(text = Mail)
        connection.close() #Close connection
        cursor.close() #Close cursor