from src.com.jalasoft.search_files.menu.menu_ui import Menu_UI
from src.com.jalasoft.search_files.search.search import Search
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.validator.validator import validator

class Menu_Search_Main(object):
    def __init__(self):
        self.menu_ui = Menu_UI()
        self.search = Search()

    def main(self):
        self.menu_ui.show_menu()