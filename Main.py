#imports - Import every class that will be used
#Each import is essentially a new window, with the exception of tkinter
#Tkinter
import tkinter as tk
#Backend
#Main Menu
import StaffMainMenu as smm
#Orders
import StaffOrder as so
import StaffOrdersView as sov
#Stock
import StaffStock as ss
import StaffIngredientAdd as sia
import StaffIngredientEdit as sie
import StaffIngredientsView as siv
#Food
import StaffFood as sf
import StaffKitMenu as skm
import StaffKitAdd as ska
import StaffKitEdit as ske
import StaffKitView as skv
import StaffRecipeMenu as srm
import StaffRecipeAdd as sra
import StaffRecipeEdit as sre
import StaffRecipeView as srv
#Accounts
import StaffAccount as sa
import StaffAccountView as sav
#Backend
#Main Menu
import ClientMainMenu as cmm 
#Orders 
import ClientOrderMenu as com 
import ClientOrderAdd as coa 
import ClientOrderEdit as coe 
import ClientOrderView as cov
#Food
import ClientFoodView as cfv 
#Account 
import ClientAccountMenu as cam 
import ClientAccountEdit as cae
import ClientAccountView as cav
import ClientDeleteCon as cdc
#Mains
import Login as l
import CreateAccount as ca
import sqlite3 as sql

#main class
#This is the parent class that every window inherits from
class window(tk.Tk):

    #initialise method
    #The class initialiser
    def __init__(
        self,
        *args,
        **kwargs
    ):

        #initialise frames
        tk.Tk.__init__(
            self,
            *args,
            **kwargs
        )

        #initialise container
        container = tk.Frame(self)
        container.pack(
            side = "top",
            fill = "both",
            expand = True
        )

        #Styling, set global background and minimum window size.
        #Minimum window size optimized for the login frame.
        self.configure(bg = "gray20")
        self.minsize(width = 626, height = 470)

        #Define a Themed Tkinter Style to use with any treeview in the program.
        #As treeviews are TTK and not just TK, typical styling configurations
        #don't apply, to change aesthetics of ttk widgets you must define 
        #custom styles
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

        #Fonts
        #LARGE FONT used with menu titles
        self.LARGE_FONT = (
            "Gisha",
            18,
            "bold"
        )
        #SMALL FONT used with other widgets like buttons, treeviews and other labels.
        self.SMALL_FONT = (
            "Gisha",
            10,
            "bold"
        )

        #Define the accountID token that will be inherited into other frames
        self.accountID = 0

        #Images
        #Logo image, used with login and main menu pages.
        self.logo = "C:\\Users\\Cormac\\Desktop\\Software\\Resources\\green_apron.gif"

        #Window Title
        self.title("Green Apron")

        #Setup frames
        #For every frame in the program, run the __init___ within the class
        self.frames = {}
        for F in (
            smm.MainMenuStaff,
            so.OrderPageStaff,
            sov.ActiveOrder,
            ss.StockPage,
            sia.AddIngredient,
            sie.EditIngredient,
            siv.ViewIngredients,
            sf.MenuPageStaff,
            skm.StaffKitsMenu,
            ska.AddKit,
            ske.StaffKitEdit,
            skv.ViewKit,
            srm.StaffRecipeMenu,
            sra.AddRecipe,
            sre.StaffRecipeEdit,
            srv.StaffRecipeView,
            sa.StaffAccount,
            sav.StaffAccountView,
            l.Login,
            cmm.MainMenuClient,
            com.ClientOrderMenu,
            coa.ClientOrderAdd,
            coe.ClientOrderEdit,
            cov.ClientOrderView,
            cfv.ClientFoodView,
            cam.ClientAccountMenu,
            cae.ClientAccountEdit,
            cav.ClientAccountView,
            ca.CreateAccount,
            cdc.ClientDeleteCon
        ):
            frame = F(
                container,
                self
            )
            self.frames[F] = frame
            frame.grid(
                row = 0,
                column = 0,
                sticky = "nsew"
            )
        #Open program on login frame
        self.show_frame(l.Login)

    #Method for transitioning between frames (or "screens" / "windows")
    #Brings selected frame to the front of the container.
    def show_frame(
        self,
        cont
    ):
        frame = self.frames[cont]
        frame.tkraise()

    #Method for validating login details, then directing user to appropriate menu
    def login(
        self,
        username,
        password,
        controller,
        aid,
    ):
        connection = sql.connect("ga.db") #Establish connection to central database
        cursor = connection.cursor() #Initialise a cursor
        #SQL Statement for reading the level associated with the
        #details entered
        fetchLevel = """SELECT level FROM CLIENT WHERE username = ?"""
        if not username == None: #username presence check
            cursor.execute(fetchLevel, (username,)) #run the SQL statement with the entered username
            level = int(cursor.fetchone()[0]) #Assign result of SQL statement to variable
            if level == 1: #If user is an employee
                self.show_frame(smm.MainMenuStaff)
            elif level == 0: #If user is a customer
                self.show_frame(cmm.MainMenuClient)
        #SQL statement for finding the account ID associated with the entered details
        fetchID = """SELECT client_id FROM CLIENT WHERE username = ?"""
        cursor.execute(fetchID, (username,)) #Run sql statement with entered username
        aid = int(cursor.fetchone()[0]) #Assign results of SQL statement to a variable
        self.accountID = aid #assign the account ID to the account ID variable within the Main
        cursor.close() #Close the connection

#UI mainlopp
app = window()
app.mainloop()
