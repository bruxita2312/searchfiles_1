from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.utils.validator import Validator
import sys
try:
    from tkinter import Tk, ttk, font, Frame, Label, Button, Entry, StringVar, DoubleVar
except ImportError:
    from Tkinter import Tk, ttk, font, Frame, Label, Button, Entry, StringVar


class Menu(object):

    def __init__(self):
        self.searching = Search()
        self.list_result = ttk.Treeview()
        self.search_window = Tk(screenName="Searcher Dana v1")
        self.window_width = int(self.search_window.winfo_screenwidth()*0.8)
        self.window_heigth = int(self.search_window.winfo_screenheight() * 0.9)
        self.search_path = Entry()
        self.search_name = Entry()
        self.search_extension = Entry()
        self.search_size = Entry()
        self.search_date = Entry()
        self.search_owner = Entry()

    """Method returns the window's width size"""

    def get_window_with(self):
        return self.window_width

    """Method returns the window's heigth size"""

    def get_window_height(self):
        return self.window_heigth

    def show_menu(self):
        """Given format to main window"""
        self.search_window.minsize(width=self.window_width, height=self.window_heigth-15)
        self.search_window.maxsize(width=self.window_width, height=self.window_heigth)
        self.search_window.title("Searcher Dana v1")
        title_frame = self.format_title_frame()
        search_frame = self.format_advance_frame()
        search_list_result = self.format_table_result()
        """Active windows"""
        self.search_window.mainloop()

    def format_title_frame(self):
        title_font = font.Font(family="Comics", size=18, weight='bold')
        title_frame = Frame(self.search_window, bd=0)
        title_frame.grid(column=0, row=0, padx=5, pady=5)
        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)
        label_title = Label(title_frame, text="Search files with:", fg="Black", font=title_font, padx=10, pady=15)
        label_title.grid(column=0, row=0, sticky="W")
        return title_frame

    def format_advance_frame(self):
        """Defining styles for labels"""
        labels_font = font.Font(family="Sans", size=11)
        """Formatting the main search frame"""
        search_frame = Frame(self.search_window, bd=2, width=self.window_width)
        search_frame.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
        search_frame.columnconfigure(0, weight=1)
        search_frame.rowconfigure(0, weight=1)
        """Labels"""
        """Defining the path where to search"""
        label_path = Label(search_frame, text="Path:", fg="Black", font=labels_font, padx=25)
        label_path.grid(column=1, row=1, sticky="W")
        self.search_path = Entry(search_frame, width=45)
        self.search_path.grid(column=2, row=1, sticky="W")
        """Defining the name to search"""
        label_name = Label(search_frame, text="Name:", fg="Black", font=labels_font, padx=25)
        label_name.grid(column=1, row=2, sticky="W")
        search_name = Entry(search_frame, width=45)
        search_name.grid(column=2, row=2, sticky="W")
        options_name = ttk.Combobox(search_frame, width=15, state="readonly")
        options_name["values"] = ["Contains", "Exact"]
        options_name.grid(column=3, row=2, sticky="E")
        """Defining the type of file to search"""
        label_extension = Label(search_frame, text="File type:", fg="Black", font=labels_font, padx=25)
        label_extension.grid(column=1, row=3, sticky="W")
        search_extension = Entry(search_frame, width=45)
        search_extension.grid(column=2, row=3, sticky="W")
        """Defining the files with size to search"""
        label_size = Label(search_frame, text="Size :", fg="Black", font=labels_font, padx=25)
        label_size.grid(column=1, row=4, sticky="W")
        search_size = Entry(search_frame, width=45)
        search_size.grid(column=2, row=4, sticky="W")
        options_size = ttk.Combobox(search_frame, width=15, state="readonly")
        options_size["values"] = ["b", "Kb", "Mb", "Gb"]
        options_size.grid(column=4, row=4, sticky="E")
        options_measure = ttk.Combobox(search_frame, width=15, state="readonly")
        options_measure["values"] = ["Equal", "Greater", "Smaller"]
        options_measure.grid(column=3, row=4, sticky="E")
        """Defining the files created on date to search"""
        label_date = Label(search_frame, text="Created on :", fg="Black", font=labels_font, padx=25)
        label_date.grid(column=1, row=5, sticky="W")
        search_date = Entry(search_frame, width=45)
        search_date.grid(column=2, row=5, sticky="W")
        """Defining the files that belongs to an owner to search"""
        label_owner = Label(search_frame, text="Owner :", fg="Black", font=labels_font, padx=25)
        label_owner.grid(column=1, row=6, sticky="W")
        search_owner = Entry(search_frame, width=45)
        search_owner.grid(column=2, row=6, sticky="W")
        """Actions buttons"""
        button_search = Button(search_frame, text="Search", command=self.action_search, bg="Light Gray")
        button_search.grid(column=3, row=8, sticky="E")
        button_clean_search = Button(search_frame, text="Clean Search fields", command=self.action_clean, bg="Light Gray")
        button_clean_search.grid(column=4, row=8, sticky="E")
        button_quit = Button(search_frame, text="Exit Search", command=self.search_window.quit, bg="Black", fg="White")
        button_quit.grid(column=5, row=8, sticky="E")
        return search_frame

    def format_table_result(self):
        result_frame = Frame(self.search_window, width=self.window_width)
        result_frame.grid(column=0, row=2, padx=(15, 15), pady=(15, 15))
        """Defining the treeview UI"""
        list_result = ttk.Treeview(result_frame, height=20)
        list_result["columns"] = ("Path", "Size", "Create Date")
        """Defining the column number"""
        list_result.column("Path", width=100)
        list_result.column("Create Date", width=50)
        list_result.column("Size", width=50)
        """Defining columns name"""
        list_result.heading("Path", text="Path")
        list_result.heading("Create Date", text="Create Date")
        list_result.heading("Size", text="Size")
        list_result.insert("", 0, text="Line 1", values=("1A", "1B"))
        list_result.grid(column=1, row=1, sticky="E")
        return result_frame

    def action_clean(self):
        pass

    def action_search(self):
        print("You press Search button")
        print("Path ", self.search_path.get())
        options = {"search_path": "d:\\MisDocs\\Fundacion\\DevFundamentals2\\", "search_on": "file", "search_name": "menu"}
        self.searching.set_options(options)
        search_results_list = []
        search_results_list=self.searching.searching()
        print("From UI the number of files/folders retrieved are:::: ", len(search_results_list))
        for for_indice in range (len(search_results_list)):
            print (for_indice)
            self.list_result.insert("", for_indice, text="Line 1", values=("1A", "1B"))
            for_indice =+ 1


if __name__ == "__main__":
    search_menu = Menu()
    search_menu.show_menu()
