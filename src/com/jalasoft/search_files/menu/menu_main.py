import sys

from src.com.jalasoft.search_files.search.search import SearchBasic
from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.validator.validator import Validator


class Menu:
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''

    def __init__(self):
        '''self.validator = Validator()'''
        #self.elections = {
         #   "1": self.search_by_name,
         #   "2": self.search_by_extension,
         #   "3": self.search_by_size,
         #   "4": self.quit
        #}

    def show_menu(self):
        print("_*_*_*_*_*_ Menu _*_*_*_*_*_")
        print(" 1 Search by Name")
        print(" 2 Search by Extension")
        print(" 3 Search by Size")
        print(" 4 quit")


    def run(self):

        while True:
            self.show_menu()
            election = int(input("enter an option:  "))
            if election==1:
                print ("** You select Search by name **")
                self.search_by_name()
                break
            elif election == 2:
                print("you select 2")
                Menu().search_by_extension()
                break
            elif election == 3:
                print("you select 3")
                Menu().search_by_size()
                break
            elif election == 4:
                print("you select 4")
                print("Bye Bye >)")
                sys.exit(0)
            elif  election >5 and election <= 9:
                print("******Please, introduce the valid value*****")
            elif election == 0:
                break
            else:
                print("miauuuuu")


    def search_by_name (self):
        search = SearchBasic()
        validator = Validator()
        path_name= input("Enter path: ")
        if validator.is_path(path_name) == True:
            name_search=input("Enter name to search: ")
            logger.info("** The path is: %s  " % path_name)
            logger.info("** The name to search is: %s  " % name_search)
            print(" ")
            print("|========= NAME ===========|====== TYPE ========|============================ PATH ===============================|")
            search._search_file_by_name(name_search, path_name)
            print("==================================================================================================")
        menu.run()



    def search_by_extension(self):
        search = SearchBasic()
        validator = Validator()
        path_name = input("Enter path: ")
        if validator.is_path(path_name) == True:
            name_search = input("Enter the extension to search: ")
            logger.info ("** The path is: " + path_name)
            logger.info ("** The extension to search is: " + name_search)
            #print("========= Search Results==========")
            print(" ")
            print("|=========NAME===========||===============================PATH===================================|")
            search._search_by_ext(name_search,path_name)
            print("===================================")
        menu.run()

    def search_by_size(self):
        search = SearchBasic()
        validator = Validator()
        path_name = input("Enter path: ")
        if validator.is_path(path_name) == True:
            name_search = input("Enter size to search (MB): ")
            logger.info ("** The path is: " + path_name)
            logger.info ("** The Size to compare is: " + name_search)
            print(" ")
            search._search_by_size(name_search,path_name)
        menu.run()

    def quit(self):
        print("Bye Bye :)")
        sys.exit(0)


if __name__ == "__main__":
    menu = Menu()
    menu.run()
