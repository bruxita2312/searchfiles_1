from os import listdir, walk, getcwd, path
from sys import exit
import logging

logging.basicConfig(filename="../../../../../log/search.log", level=logging.DEBUG, format='%(levelname)s : %(asctime)s : %(message)s')

class Search(object):

    def __init__(self, path):
        self.path = path
        self.result = {}

    def options(self, option, text=None):
        if (option == 1):
            self._search_file_by_name(text)
        elif (option == 2):
            self._search_by_size(text)
        elif (option == 3):
            self._search_folder_by_name(text)
        else:
            print("Exiting from searcher")
            exit(0)

    def _search_by_name(self, text):
        for search_path, folders, files in walk(self.path):
            for fil in files:
                fil_search_path = path.join(search_path,fil)
                if path.isfile(fil_search_path):
                    if text in fil_search_path:
                        print ("OBJECT::: ", fil_search_path)

    def _search_file_by_name(self, text):
        logging.info("Searching files naming %s"  %text)
        for search_path, folders, files in walk(self.path):
            for fil in files:
                fil_search_path = path.join(search_path,fil)
                if path.isfile(fil_search_path) and text in fil:
                    logging.debug ("FILE::: %s  " %fil_search_path)
                    # myfile = MyFile()
                    # myfile.set_name(fil)
                    # myfile.set_path(search_path)
                    # myfile.set_size(int(path.getsize(fil_search_path)))
                    # self.result.append(myfile)

    def _search_folder_by_name(self, text):
        logging.info("Searching folders naming %s"  %text)
        for search_path, folders, files in walk(self.path):
            for fol in folders:
                fol_search_path = path.join(search_path,fol)
                if path.isdir(fol_search_path):
                    if text in fol:
                        logging.debug("FOLDER::: %s " %fol_search_path)

    def _search_by_size(self, text):
        logging.info("Searching files with size %d" % int(text))
        for search_path, folders, files in walk(self.path):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if path.isfile(fil_search_path) and int(path.getsize(fil_search_path)) == int(text):
                    logging.debug("FILE::: %s  ::::: SIZE::::: %d" % (
                    fil_search_path, int(path.getsize(fil_search_path))))
                    # myfile = MyFile()
                    # myfile.set_name(fil)
                    # myfile.set_path(search_path)
                    # myfile.set_size(int(path.getsize(fil_search_path)))
                    # self.result.append(myfile)

if __name__ == "__main__":
    search = Search("d:/")
    search.options(1, "sales")
    search.options(3, "one")
    search.options(2, "9968")
    search.options(4)
