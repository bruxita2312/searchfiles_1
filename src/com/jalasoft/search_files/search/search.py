from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
from os import walk, path


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
                result = SearchResult()
                aux_search_path = path.join(search_path, fil)
                if path.isfile(aux_search_path):
                    result.set_name(fil)
                    result.set_path(search_path)
                    result.set_type(get_extension(aux_search_path))
                    result.set_size(int(path.getsize(aux_search_path)))
                    result.set_cdate(timestamp_to_date(path.getctime(aux_search_path)))
                    result.set_abspath(aux_search_path)
                    result.set_ftype("file")
                    add_to_list = self.add_to_results(result)
                    if add_to_list == True:
                        logger.info(":::: %s \t || %s \t || %d \t || %s \t || %s \t || %s" % (result.get_name(), result.get_type(), result.get_size(), result.get_cdate(), result.get_ftype(), result.get_abspath()))
                        results.append(result)
            for fil in folders:
                result = SearchResult()
                aux_search_path = path.join(search_path, fil)
                if path.isdir(aux_search_path):
                    result.set_name(fil)
                    result.set_path(search_path)
                    result.set_abspath(aux_search_path)
                    result.set_size(int(path.getsize(aux_search_path)))
                    result.set_cdate(path.getctime(aux_search_path))
                    result.set_ftype("folder")
                    add_to_list = self.add_to_results(result)
                    if add_to_list == True:
                        logger.info("FOLDER:::: %s \t || %s \t || %d \t || %s \t || %s \t || %s" % (result.get_name(), result.get_path(), result.get_size(), result.get_cdate(), result.get_ftype(), result.get_abspath()))
                        results.append(result)
        logger.info("SEARCHING RESULT TOTAL ::: %d" % int(len(results)))
        logger.info("SEARCHING end")
        logger.info("\n++++++++++++++++++++++++++++++++++++\n====================================\n--------------------------")
        return results

    def add_to_results(self, result):
        boolean_name = self.search_by_name(result)
        boolean_size = self.search_by_size(result)
        boolean_ext = True
        if path.isfile(result.get_abspath()):
            boolean_ext = self.search_by_extension(result)
        boolean_ctime = self.search_by_date(result)
        #boolean_ctime = True
        if boolean_name == True and boolean_size == True and boolean_ext==True and boolean_ctime==True:
            return True
        else:
            return False

    """This method allows to make search by name"""
    def search_by_name(self, search_result):
        name = ""
        if path.isfile(search_result.get_abspath()):
            name = get_filename(search_result.get_name(),search_result.get_type())
        if path.isdir(search_result.get_abspath()):
            name = search_result.get_abspath()
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
                    if self.options.get("search_name") in name:
                        return True
                    else:
                        return False
            else:
                if self.options.get("search_name") in name:
                    return True
                else:
                    return False
        else:
            return True

    """Allows to search by size any file or folder"""
    def search_by_size(self, search_result):
        if "search_size" in self.options.keys():
            if "search_size_options" in self.options.keys():
                if self.options.get("search_size_options") == "Greater":
                    if search_result.get_size() >= int(self.options.get("search_size")):
                        logger.info("SEARCH SIZE OPTION ::: \t %d ::: \t %s ::: \t %d \t(%s)" % (
                            self.options.get("search_size"), self.options.get("search_size_options"), search_result.get_size(), search_result.get_name()))
                        return True
                    else:
                        return False
                elif self.options.get("search_size_options") == "Smaller":
                    if search_result.get_size() <= int(self.options.get("search_size")):
                        logger.info("SEARCH SIZE OPTION ::: \t %d ::: \t %s ::: \t %d \t(%s)" % (
                        self.options.get("search_size"), self.options.get("search_size_options"), search_result.get_size(), search_result.get_name()))
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
                    logger.info("SEARCH SIZE OPTION ::: \t %d ::: \t %s ::: \t %d \t(%s)" % (
                        self.options.get("search_size"), self.options.get("search_size_options"), search_result.get_size(), search_result.get_name()))
                    return True
                else:
                    return False
        else:
            return True

    """Allows to search by create date any file or folder"""
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

    """Allows to search by extension/filetype any file"""
    def search_by_extension(self, result):
        search_result = result
        if "search_type" in self.options.keys():
            if self.options.get("search_type") in search_result.get_ftype():
                return True
            else:
                return False
        else:
            return True

if __name__ == "__main__":
    """Test search by name and size"""
    options3 = {"search_path": "e:\\", "search_on": "file", "search_size": size_converter_to_bytes(14.0066,"mb"), "search_size_options":"Equal"}
    options4 = {"search_path": "e:\\", "search_on": "file", "search_size": size_converter_to_bytes(950,"mb"),"search_size_options":"Greater"}
    options5 = {"search_path": "e:\\", "search_on": "file", "search_size": size_converter_to_bytes(35,"mb"),"search_size_options":"Smaller"}
    searcha = Search()
    searcha.set_options(options5)
    searcha.searching()
