from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
from src.com.jalasoft.search_files.validator.validator import Validator
from os import walk, path, stat


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
        self.search_results = results

    def searching(self):
        logger.info("SEARCHING begin")
        results = []
        if "search_path" not in self.options.keys():
            self.options["search_path"] = "/"
        for search_path, folders, files in walk(self.options.get("search_path")):
            for fil in files:
                try:
                    result = SearchResult()
                    search_path = path.join(search_path, fil)
                    result.set_name(fil)
                    result.set_path(search_path)
                    result.set_type(get_extension(search_path))
                    result.set_size(int(path.getsize(search_path)))
                    result.set_cdate(timestamp_to_date(path.getctime(search_path)))
                    logger.info("FILE :::: %s \t || %s \t || %d \t || %s" %(result.get_name(), result.get_path(),result.get_size(),result.get_cdate()))
                    add_to_list = self.add_to_results(result)
                    if add_to_list == True:
                        result.set_ftype("file")
                        result.set_owner(stat(fil).st_uid)
                        results.append(result)
                except FileNotFoundError :
                    logger.error("FAILED ON FILE::: %s" %fil)
            for fil in folders:
                try:
                    result = SearchResult()
                    search_path = path.join(search_path, fil)
                    result.set_name(fil)
                    result.set_path(search_path)
                    logger.info("FOLDER :::: %s \t || %s \t || %d \t || %s" %(result.get_name(), result.get_path(),result.get_size(),result.get_cdate()))
                    add_to_list = self.add_to_results(result)
                    if add_to_list == True:
                        result.set_ftype("folder")
                        results.append(result)
                except FileExistsError:
                    logger.error("FAILED ON FOLDER::: %s" % fil)
        logger.info("SEARCHING end")
        return results

    def add_to_results(self, result):
        boolean_name = True
        boolean_size = True
        boolean_ext=True
        boolean_ctime = True
        if boolean_name==True and boolean_ext==True and boolean_size==True and boolean_ctime == True:
            return True
        else:
            return False

    def search_by_name(self, result):
        search_result = result
        name = get_name(search_result.get_name())
        if "search_name" in self.options.keys():
            if "search_name_options" in self.options.keys():
                if self.options.get("search_name_options") == "Exact":
                    if self.options.get("search_name") == name:
                        return True
                    else:
                        return False
                elif self.options.get("search_name_options") == "Contains":
                    if self.options.get("search_name") in name:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return True
        else:
            return True

    def search_by_size(self, result):
        search_result = result
        if "search_size" in self.options.keys():
            if "search_size_options" in self.options.keys():
                if self.options.get("search_size_options") == "Greater":
                    if search_result.get_size() > int(self.options.get("search_size")):
                        return True
                    else:
                        return False
                elif "Smaller" in self.options:
                    if search_result.get_size() < int(self.options.get("search_size")):
                        return True
                    else:
                        return False
                else:
                    if search_result.get_size() == int(self.options.get("search_size")):
                        return True
                    else:
                        return False
            else:
                if search_result.get_size() == int(self.options.get("search_size")):
                    return True
                else:
                    return False
        else:
            return True

    def search_by_date(self, result):
        search_result = result
        if "search_date" in self.options.keys():
            if "search_date_options" in self.options.keys():
                if "Greater" in self.options:
                    if search_result.get_ctime() > self.options.get("search_date"):
                        return True
                    else:
                        return False
                elif "Smaller" in self.options:
                    if search_result.get_ctime() < self.options.get("search_date"):
                        return True
                    else:
                        return False
                else:
                    if search_result.get_ctime() == self.options.get("search_date"):
                        return True
                    else:
                        return False
            else:
                if search_result.get_ctime() == self.options.get("search_date"):
                    return True
                else:
                    return False
        else:
            return True

    def search_by_extension(self, result):
        search_result = result
        if "search_type" in self.options.keys():
            if self.options.get("search_type") in search_result.get_ftype():
                return True
            else:
                return False
        else:
            return True

    def search_by_owner(self, result):
        pass


if __name__ == "__main__":
    """Test search by name"""
    options = {"search_path":"d:\\MisDocs\\Fundacion\\DevFundamentals2", "search_on":"file","search_name":"menu"}
    """Test search by name and size"""
    options2 = {"search_path": "d:\\MisDocs\\Fundacion\\DevFundamentals2", "search_on": "file", "search_name": "menu","search_size": 1037}
    options3 = {"search_path": "d:\\MisDocs\\Fundacion\\DevFundamentals2", "search_on": "file", "search_name": "searc", "search_size": 1500,"search_size_options":"Greater"}
    searcha = Search()
    searcha.set_options(options)
    searcha.searching()
    searcha.set_options(options3)
    searcha.searching()
