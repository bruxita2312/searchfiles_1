import logging
from datetime import datetime
from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from os import listdir, walk, getcwd, path
from sys import exit

logging.basicConfig(filename="../../../../../log/search.log", level=logging.DEBUG,
                    format='%(levelname)s : %(asctime)s : %(message)s')


class Search(object):

    def __init__(self):
        self.options = {}
        self.search_results = []

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options

    def get_search_results(self):
        return self.search_results

    def set_search_results(self, results):
        self.search_results=results

    def search_options(self):
        logging.info("SEARCH_OPTIONS begin")
        try:
            if self.options.get("type") == "basic":
                logging.info("BASIC SEARCH:::")
                # option = self.options.get("option")
                # logging.info("CRITERIA::: %s  " % option)
                # text = self.options.get("text")
                # logging.info("CRITERIA::: %s  " % text)
                # searchpath = self.options.get("path")
                # logging.info("PATH::: %s  " % searchpath)
                # operator = self.options.get("operator")
                # b_options = {'option': self.options.get("option"), 'path': self.options.get("path"), 'text':, 'operator':}
                #self.set_search_results(self.basic_search(self.options))
            else:
                logging.info("ADVANCED SEARCH:::")
                #self.set_search_results(self.adv_search(self.options))
        except:
            pass
        logging.info("SEARCH_OPTIONS end")

    def searching(self):
        logging.info("SEARCHING begin")
        results=[]
        if self.options.get("path") == None or "path" not in self.options:
            self.options["path"]="/"
        for search_path, folders, files in walk(self.options.get("search_path")):
            result = SearchResult()
            for fil in files:
                search_path = path.join(search_path, fil)
                result.set_name(fil)
                result.set_path(search_path)
                result.set_type(get_extension(search_path))
                result.set_ftype("file")
                result.set_size(int(path.getsize(search_path)))
                result.set_abspath(path.abspath(search_path))
                result.set_cdate(timestamp_to_date(path.getctime(search_path)))
                results.append(result)
                result = SearchResult()
            for fil in folders:
                search_path = path.join(search_path, fil)
                result.set_name(fil)
                result.set_path(search_path)
                result.set_ftype("folder")
                result.set_size(int(path.getsize(search_path)))
                result.set_abspath(path.abspath(search_path))
                result.set_cdate(timestamp_to_date(path.getctime(search_path)))
                results.append(result)
                result = SearchResult()
        logging.info("SEARCHING end")
        return results

    def search_by_name(self,result):
        search_result = SearchResult()
        search_result=result
        name = get_name(search_result.get_name())
        if "name" in self.options:
            if self.options.get("name") in name:
                return True
            else:
                return False
        else:
            return True

    def search_by_size(self,result):
        search_result = SearchResult()
        search_result=result
        if "size" in self.options:
            if "greater" in self.options:
                if search_result.get_size() > int(self.options.get("size")):
                    return True
                else:
                    False
            elif "less" in self.options:
                if search_result.get_size() < int(self.options.get("size")):
                    return True
                else:
                    False
            else:
                if search_result.get_size() == int(self.options.get("size")):
                    return True
                else:
                    False
        else:
            return True

    def search_by_date(self,result):
        search_result = SearchResult()
        search_result = result
        if "date" in self.options:
            if "greater" in self.options:
                if search_result.get_ctime() > self.options.get("date"):
                    return True
                else:
                    False
            elif "less" in self.options:
                if search_result.get_ctime() < self.options.get("date"):
                    return True
                else:
                    False
            else:
                if search_result.get_ctime() == self.options.get("date"):
                    return True
                else:
                    False
        else:
            return True

    def search_by_extension(self,result):
        search_result = SearchResult()
        search_result = result
        if "type" in self.options:
            if self.options.get("type") in search_result.get_ftype():
                return True
            else:
                False
        else:
            return True


    """def _search_file_by_name(self, text, pos):
        logging.info("Searching files naming %s" % text)
        results = []
        for search_path, folders, files in walk(self.path):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if path.isfile(fil_search_path) and text in fil:
                    logging.debug("FILE::: %s  " % fil_search_path)
                    myfile = SearchFile(fil, search_path)
                    myfile.set_size(int(path.getsize(fil_search_path)) / 1024)
                    myfile.set_abspath(path.abspath(fil_search_path))
                    ctime = datetime.fromtimestamp(path.getctime(fil_search_path)).strftime('%Y-%m-%d %H:%M:%S')
                    myfile.set_cdate(ctime)
                    results.append(myfile)
        return results"""

    """def _search_folder_by_name(self, text, pos):
        logging.info("Searching folders naming %s" % text)
        for search_path, folders, files in walk(self.path):
            for fol in folders:
                fol_search_path = path.join(search_path, fol)
                if path.isdir(fol_search_path):
                    if text in fol:
                        logging.debug("FOLDER::: %s " % fol_search_path)"""

    """def _search_by_size(self, path, size, operator):
        logging.info("SEARCH BY SIZE %d" % int(size))
        for search_path, folders, files in walk(self.path):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if path.isfile(fil_search_path) and int(path.getsize(fil_search_path)) == int(size):
                    logging.debug("FILE::: %s  ::::: SIZE::::: %d" % (
                        fil_search_path, int(path.getsize(fil_search_path))))"""

    def _search_by_extension(self, path, extension, operator):
        pass

    def _search_by_date(self, path, date, operator):
        pass


if __name__ == "__main__":
    search = Search()
    # search.options(1, "sales")
    # search.options(3, "one")
    # search.options(2, "9968")
    # search.options(4)
