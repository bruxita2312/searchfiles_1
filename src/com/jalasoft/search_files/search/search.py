from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
from os import listdir, walk, getcwd, path


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
        logger.info("SEARCH_OPTIONS begin")
        try:
            if self.options.get("type") == "basic":
                logger.info("BASIC SEARCH:::")
                #self.set_search_results(self.basic_search(self.options))
            else:
                logger.info("ADVANCED SEARCH:::")
                #self.set_search_results(self.adv_search(self.options))
        except:
            pass
        logger.info("SEARCH_OPTIONS end")

    def searching(self):
        logger.info("SEARCHING begin")
        results=[]
        if self.options.get("path") == None or "path" not in self.options:
            self.options["path"]="/"
        for search_path, folders, files in walk(self.options.get("search_path")):
            for fil in files:
                result = SearchResult()
                search_path = path.join(search_path, fil)
                result.set_name(fil)
                result.set_path(search_path)
                result.set_type(get_extension(search_path))
                result.set_ftype("file")
                result.set_size(int(path.getsize(search_path)))
                result.set_abspath(path.abspath(search_path))
                result.set_cdate(timestamp_to_date(path.getctime(search_path)))
                results.append(result)
            for fil in folders:
                result = SearchResult()
                search_path = path.join(search_path, fil)
                result.set_name(fil)
                result.set_path(search_path)
                result.set_ftype("folder")
                result.set_size(int(path.getsize(search_path)))
                result.set_abspath(path.abspath(search_path))
                result.set_cdate(timestamp_to_date(path.getctime(search_path)))
                results.append(result)
        logger.info("SEARCHING end")
        return results

    def search_by_name(self,result):
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
        search_result = result
        if "type" in self.options:
            if self.options.get("type") in search_result.get_ftype():
                return True
            else:
                False
        else:
            return True

if __name__ == "__main__":
    search = Search()
    options = {"path": "C:/", "name":"algo",}
    # search.options(1, "sales")
    # search.options(3, "one")
    # search.options(2, "9968")
    # search.options(4)
