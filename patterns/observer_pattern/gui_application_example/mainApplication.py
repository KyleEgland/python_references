#! python3
#
# Main program for a GUI with tkinter
# Import information
# tkinter = GUI module, used to construct GUI
# ttk = tkinter styling module, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
from primarytab import PrimaryTab
from alternatetab import AlternateTab


class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Give the window an icon (must be in dir desginated)
        # tk.Tk.iconbitmap(self, default='icons/example_icon.ico')
        # Give the window a title (displayed in title bar; top of window)
        tk.Tk.wm_title(self, 'Example GUI')

        # Create the Notebook widget that will comprise the main part
        # of the application
        self.notebook = ttk.Notebook(self)
        # Use pack geometry to fill window with the Notebook widget
        self.notebook.pack(fill='both', expand=True)

        # Instantiate Notebook pages, note that the order here determines load
        # order - this can be important depending on desired effect(s)
        primary_tab = PrimaryTab(self.notebook)
        alt_tab = AlternateTab(self.notebook)

        # Add the pages to the Notebook; this order determines appearnce on
        # the window - it can be specified explicitely as well
        self.notebook.add(primary_tab, text='Main')
        self.notebook.add(alt_tab, text='Alternate')

        # Top menu bar (e.g. File, Edit, etc.)
        # Menu bar will be visible across all tabs as when it is placed here
        # in the "Main window"
        menu_bar = tk.Menu(self)

        # Creating menus for the menu bar
        # "file_menu" instantiates the variable that is to serve as the actual
        # "File" menu.  Using "tearoff=0" prevents it from being moved -
        # meaning clicked and dragged to somewhere else
        file_menu = tk.Menu(menu_bar, tearoff=0)

        # Creating commands to house inside menus of menu bar
        file_menu.add_command(label='New Thing', accelerator='Ctrl+N')
        file_menu.add_command(label='Load Thing', accelerator='Ctrl+L')
        file_menu.add_command(label='Save Thing', accelerator='Ctrl+S')

        # Adding menus to menu bar
        # Add cascade to allow cascade effect over window.
        # Cascade effect is the "normal" file menu effect
        menu_bar.add_cascade(label='File', underline=0, menu=file_menu)
        # Identify "menu_bar" as the menu for the application
        self.config(menu=menu_bar)


app = MyApp()
app.mainloop()
