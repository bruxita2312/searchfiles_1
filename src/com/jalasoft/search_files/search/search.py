from os import listdir, walk, getcwd
from os.path import isfile, join, isdir, exists, getsize
from sys import exit

class Search:

    def __init__(self):
        current_path = getcwd()
        print('I am on %s ' % current_path)
        print("""
                         Search Menu
                         1 Search by name
                         2 Search by side
                         3 Search by extension
                         4 Exit
                         """)

    def options(self, option, name=None, size=0, type=None, path="/"):
        if (option == 1):
            self.search_file_by_name(name, path)
        elif (option == 2):
            self.search_by_size(size, path)
        elif (option == 3):
            self.search_by_extension(type, path)
        else:
            print("Exiting from searcher")
            exit(0)

    def search_file_by_name(self, name, path=None):
        print("This is search file by name")
        for mfile in listdir(path):
            print("FILE ::: ", type(mfile))
        print('Another method')
        #for (path, ficheros, archivos) in walk(path):
            #print(path)
            #print(ficheros)
            #print(archivos)

    def search_folder_by_name(self, name, path="/"):
        print("This is search folder by name")

    def search_by_extension(self, type, path="/"):
        print("This is search file by type")

    def search_by_size(self, size, path="/"):
        print("This is search file by size")


if __name__ == "__main__":
    search = Search()
    search.options(1, "file_name", getcwd())
    #search.options(1, "file_name", "C:/Users")
    #search.options(1, "file_name", "/")
    search.options(2, 1525, "/")
    search.options(3, "txt", "D:/")
    search.options(4)
