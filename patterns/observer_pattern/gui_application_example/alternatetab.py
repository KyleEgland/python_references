#! python3
#
# Primary tab for mainApplication of example GUI
# Import information:
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
import varserver


class AlternateTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure" tell the program
        # how to resize widgets when the window is resized
        # Weight affects how the item will be scaled in relation
        # to the other elements that are bing re-sized
        # E.g. a row with weight 1 will scale more than a row with weight 2
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)

        # Row 0
        # A status
        # Labels are static text, they don't update unless you force them
        # This label displays the text noted in its instantiation line.
        self.btn_click_lbl = tk.Label(self, text='Number of button clicks:')
        # Grid is a geometry method that allows the coder to dictate widget
        # location, size (to a certain extent), and alignment.  Below, the row
        # and column number (everything begins with 0) are specified to dictate
        # where this widget should exist.  After that, the "sticky" alignment
        # is dictated; sticky will stretch widgets like buttons but center
        # widgets like labels.  In this case, 'sne' will align the text between
        # the top and bottom of the cell (sn = south north) and keep the text
        # to the far right of the cell (e = east).
        self.btn_click_lbl.grid(row=0, column=0, sticky='sne', padx=5, pady=5)

        # The IntVar and StringVar are special tkinter variables that allow
        # the coder to "track" variable changes.  This IntVar is used to force
        # update the label "btn_click_status" without using extra lines of code
        self.btn_click_num = tk.IntVar()
        btn_num = varserver.Watcher(self.btn_click_num)
        varserver.click_num.attach(btn_num)
        self.btn_click_num.set(str(btn_num.currentval()))

        # This label displays the number of clicks as an integer and is getting
        # its value from the IntVar created above
        self.btn_click_status = tk.Label(self, textvariable=self.btn_click_num)
        self.btn_click_status.grid(
            row=0, column=1, sticky='nsw', padx=5, pady=5)

        # Row 1
        # Buttons
        # There are tkinter buttons and ttk buttons.  The difference is that
        # the ttk buttons are a little more modern looking and adapt better
        # on newer systems, such as Windows 10
        # Also note that a command is attached here to the button.  This
        # command, by default, is triggered by a LEFT click.
        self.add_btn = ttk.Button(
            self, text='+', command=self.add_one)
        self.add_btn.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.sub_btn = ttk.Button(self, text='-', command=self.sub_one)
        self.sub_btn.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

    def add_one(self):
        # new_num = self.btn_click_num.get() + 1
        # self.btn_click_num.set(new_num)
        varserver.click_num.addOne()

    def sub_one(self):
        varserver.click_num.subOne()
