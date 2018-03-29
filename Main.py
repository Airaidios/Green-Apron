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
"""#Backend
#Main Menu
import ClientMainMenu as cmm 
#Orders 
import ClientOrderMenu as com 
import ClientOrderAdd as coa 
import ClientOrderEdit as coe 
#Food
import ClientFoodView as cfv 
#Account 
import ClientAccountMenu as cam 
import ClientAccountEdit as cae"""
#Mains
import Login as l
"""import CreateAccount as ca"""

#main class
#This is the parent class that every window imports from
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

        #Window icon - Currently broken, don't know why
        """
        self.iconbitmap(default = "icon.bmp")
        """

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

        #Images
        #Logo image, used with login and main menu pages.
        self.logo = "C:\\Users\\Cormac\\Desktop\\Software\\Resources\\green_apron.gif"

        #Window Title
        self.title("Green Apron")

        #Setup frames
        #Initialises the child classes (this encompasses all used screens)
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
        self.show_frame(l.Login)

    #Method for transitioning between frames (or "screens" / "windows")
    def show_frame(
        self,
        cont
    ):
        frame = self.frames[cont]
        frame.tkraise()

app = window()
app.mainloop()
