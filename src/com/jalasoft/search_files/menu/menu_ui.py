from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.validator.validator import Validator
from src.com.jalasoft.search_files.utils.search_util import *
import sys

try:
    from tkinter import Tk, ttk, font, Frame, Label, Button, Entry, StringVar, DoubleVar
except ImportError:
    from tkinter import Tk, ttk, font, Frame, Label, Button, Entry, StringVar


class Menu_UI(object):

    def __init__(self):
        self.searching = Search()
        self.list_result = ""
        self.search_window = Tk(screenName="SEARCH")
        self.window_width = int(self.search_window.winfo_screenwidth() * 0.5)
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

    """Method that displays the UI"""

    def show_menu(self):
        """Given format to main window"""
        self.search_window.minsize(width=self.window_width, height=self.window_heigth - 15)
        self.search_window.maxsize(width=self.window_width * 2, height=self.window_heigth)
        self.search_window.title("SEARCH")
        self.format_title_frame()
        self.format_advance_frame()
        self.format_table_result()
        """Active windows"""
        self.search_window.mainloop()

    """Method that formatted and packed element for the windows title"""

    def format_title_frame(self):
        title_font = font.Font(family="Comics", size=18, weight='bold')
        title_frame = Frame(self.search_window, bd=0)
        title_frame.grid(column=0, row=0, padx=2, pady=2)
        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)
        label_title = Label(title_frame, text="Search files with:", fg="Black", font=title_font, padx=10, pady=15)
        label_title.grid(column=0, row=0, sticky="W")

    """Method that formatted and packed element for the windows search panel"""

    def format_advance_frame(self):

        self.path_by_default=StringVar()
        self.path_by_default.set("/Users/dxnis/Documents/pruebamenu")
        self.options_name_by_default=StringVar()
        self.options_name_by_default.set("Contains")
        self.options_size_by_default=StringVar()
        self.options_size_by_default.set=("Kbyte")
        self.options_measure_by_default=StringVar()
        self.options_measure_by_default.set=("Smaller")



        """Defining styles for labels"""
        labels_font = font.Font(family="Sans", size=11)
        """Formatting the main search frame"""
        search_frame = Frame(self.search_window, bd=2, width=self.window_width)
        search_frame.grid(column=0, row=1, padx=(5, 5), pady=(5, 5))
        search_frame.columnconfigure(0, weight=1)
        search_frame.rowconfigure(0, weight=1)

        """Labels"""
        """Defining the path where to search"""
        label_path = Label(search_frame, text="Path:", fg="Black", font=labels_font, padx=25)
        label_path.grid(column=1, row=1, sticky="W")
        self.search_path = Entry(search_frame, width=45, textvariable=self.path_by_default)
        self.search_path.grid(column=2, row=1, sticky="W")

        """Defining the name to search"""
        label_name = Label(search_frame, text="Name:", fg="Black", font=labels_font, padx=25)
        label_name.grid(column=1, row=2, sticky="W")
        self.search_name = Entry(search_frame, width=45)
        self.search_name.grid(column=2, row=2, sticky="W")
        self.options_name = ttk.Combobox(search_frame, width=15, state="readonly", textvariable=self.options_name_by_default)
        self.options_name["values"] = ["Contains", "Exact"]
        self.options_name.grid(column=3, row=2, sticky="E")

        """Defining the type of file to search"""
        label_extension = Label(search_frame, text="File type:", fg="Black", font=labels_font, padx=25)
        label_extension.grid(column=1, row=3, sticky="W")
        self.search_extension = Entry(search_frame, width=20)
        self.search_extension.grid(column=2, row=3, sticky="W")

        """Defining the files with size to search"""
        label_size = Label(search_frame, text="Size :", fg="Black", font=labels_font, padx=25)
        label_size.grid(column=1, row=4, sticky="W")
        self.search_size = Entry(search_frame, width=20)
        self.search_size.grid(column=2, row=4, sticky="W")
        self.options_size = ttk.Combobox(search_frame, width=15, state="readonly", textvariable=self.options_size_by_default)
        self.options_size["values"] = ["byte", "Kbyte", "Mbyte", "Gbyte"]
        self.options_size.grid(column=4, row=4, sticky="E")
        self.options_measure = ttk.Combobox(search_frame, width=15, state="readonly", textvariable=self.options_measure_by_default)
        self.options_measure["values"] = ["Equal", "Greater", "Smaller"]
        self.options_measure.grid(column=3, row=4, sticky="E")

        """Defining the files created on date to search"""
        #label_date = Label(search_frame, text="Created on :", fg="Black", font=labels_font, padx=25)
        #label_date.grid(column=1, row=5, sticky="W")
        #self.search_date = Entry(search_frame, width=20)
        #self.search_date.grid(column=2, row=5, sticky="W")

        """Actions buttons"""
        button_search = Button(search_frame, text="Search", command=self.action_search, bg="Light Gray")
        button_search.grid(column=3, row=8, sticky="E")
        button_clean_search = Button(search_frame, text="CLEAN", command=self.action_clean, bg="Light Gray")
        button_clean_search.grid(column=4, row=8, sticky="E")
        button_quit = Button(search_frame, text="QUIT", command=self.search_window.quit, bg="Black", fg="White")
        button_quit.grid(column=5, row=8, sticky="E")
        return search_frame


    """Method that formatted and packed element for the search results"""

    def format_table_result(self):
        self.result_frame = Frame(self.search_window, width=self.window_width * 2, bg="Gray")
        self.result_frame.grid(column=0, row=2)
        """Defining the treeview UI"""
        self.list_result = ttk.Treeview(self.result_frame, selectmode="browse")
        vsb = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.list_result.yview)
        self.list_result.configure(yscrollcommand=vsb.set)
        self.list_result["columns"] = ("Path", "Size", "Create Date")
        """Defining the column number"""

        self.list_result.column("Path", width=250)
        self.list_result.column("Create Date", width=150)
        self.list_result.column("Size", width=100)
        """Defining columns name"""
        self.list_result.heading("Path", text="Path")
        self.list_result.heading("Create Date", text="Create Date")
        self.list_result.heading("Size", text="Size (Mb)")
        self.list_result.grid(column=1, row=1, sticky="NSWE")
        vsb.grid(column=2, row=1, sticky="NES")
        return self.result_frame

    def action_clean(self):
        self.path_by_default.set("/Users/dxnis/Documents/pruebamenu")
        self.search_name.delete(0,'end')
        self.search_extension.delete(0,'end')
        self.search_size.delete(0,'end')


    """Method that creates the options map and calls the searching method of the Search class"""


    #click Search button
    def action_search(self):

        """Add validators to lunch search process"""
        "get all values"

        _size=self.search_size.get()
        _size_measure = self.options_measure.get()
        _size_option=self.options_size.get()

        #print(_path,_name,_name_option,_extension,_size, _size_option ,_size_measure)
        validate = Validator()

        """Test search by name"""
        _search_general={"search_path": self.search_path.get(),"search_on":"file", "search_name": self.search_name.get(),"search_name_options": self.options_name.get(), "search_by_extension":self.search_extension.get(), "search_size": self.search_size.get(), "search_size_options": self.options_measure.get(), }


        self.searching.set_options(_search_general)
        self.search_results_list = []
        self.search_results_list.clear()
        self.search_results_list = self.searching.searching()
        print("From UI the number of files/folders retrieved are:::: ", len(self.search_results_list))
        for s_result in self.search_results_list:
            pass
        for for_indice in range(len(self.search_results_list)):
            self.list_result.insert("", for_indice, text=self.search_results_list[for_indice].get_name(), values=(
                self.search_results_list[for_indice].get_path(), size_converter(self.search_results_list[for_indice].get_size(), "mb"), self.search_results_list[for_indice].get_cdate()))
            for_indice = for_indice + 1


if __name__ == "__main__":
    search_menu = Menu_UI()
    search_menu.show_menu()
