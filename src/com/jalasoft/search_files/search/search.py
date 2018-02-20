from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
from os import walk, path


class Search(object):

    def __init__(self):
        self.options = {}
        self.search_results = []

    def get_options(self):
        """Returns the criteria search"""
        return self.options

    def set_options(self, options):
        """Sets the criteria search"""
        self.options = options

    def get_search_results(self):
        """Returns the search result list"""
        return self.search_results

    def set_search_results(self, results):
        """Sets the search results list"""
        self.search_results = results

    def searching(self):
        """Start the search process acorrding the criteria search set"""
        logger.info("SEARCHING::: begin")
        results = []
        logger.info("Criteria search %s" % str(self.get_options()))
        if "search_path" not in self.options.keys():
            self.options["search_path"] = "/"
        for search_path, folders, files in walk(self.options.get("search_path")):
            if self.options.get("search_on") == "File" or self.options.get("search_on") == "Both":
                for fil in files:
                    result = SearchResult()
                    aux_search_path = path.join(search_path, fil)
                    if path.isfile(aux_search_path):
                        result.set_name(fil)
                        result.set_path(search_path)
                        result.set_type(get_extension(aux_search_path))
                        result.set_size(int(path.getsize(aux_search_path)))
                        result.set_cdate(timestamp_to_date(path.getctime(aux_search_path)))
                        result.set_mdate(timestamp_to_date(path.getmtime(aux_search_path)))
                        result.set_abspath(aux_search_path)
                        result.set_ftype("file")
                        add_to_list = self.add_to_results(result)
                        if add_to_list == True:
                            logger.info("FILE:::: %s \t || %s \t || %d \t || %s \t || %s \t || %s" % (result.get_name(), result.get_type(), result.get_size(), result.get_cdate(), result.get_ftype(), result.get_abspath()))
                            results.append(result)
            if self.options.get("search_on") == "Folder" or self.options.get("search_on") == "Both":
                for fil in folders:
                    result = SearchResult()
                    aux_search_path = path.join(search_path, fil)
                    if path.isdir(aux_search_path):
                        result.set_name(fil)
                        result.set_path(search_path)
                        result.set_abspath(aux_search_path)
                        result.set_size(int(path.getsize(aux_search_path)))
                        result.set_cdate(path.getctime(aux_search_path))
                        result.set_mdate(timestamp_to_date(path.getmtime(aux_search_path)))
                        result.set_ftype("folder")
                        add_to_list = self.add_to_results(result)
                        if add_to_list == True:
                            logger.info("FOLDER:::: %s \t || %s \t || %d \t || %s \t || %s \t || %s" % (result.get_name(), result.get_path(), result.get_size(), result.get_cdate(), result.get_ftype(), result.get_abspath()))
                            results.append(result)
        logger.info("RESULT TOTAL ::: %d" % int(len(results)))
        logger.info("SEARCHING::: end")
        logger.info("\n++++++++++++++++++++++++++++++++++++\n==========================\n--------------------")
        return results

    def add_to_results(self, result):
        boolean_name = self.search_by_name(result)
        boolean_size = self.search_by_size(result)
        boolean_ext = False
        boolean_ctime = False
        if path.isfile(result.get_abspath()):
            boolean_ext = self.search_by_extension(result)
            boolean_ctime = self.search_by_date(result)
        if boolean_name == True and boolean_size == True and boolean_ext==True and boolean_ctime==True:
            logger.info("ADD TO RESULTS ::: TRUE")
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
                        logger.info("SEARCH BY NAME EXACT :::: True")
                        return True
                    else:
                        return False
                elif self.options.get("search_name_options") == "Contains":
                    if self.options.get("search_name") in name:
                        logger.info("SEARCH BY NAME CONTAINS :::: True")
                        return True
                    else:
                        return False
                else:
                    if self.options.get("search_name") in name:
                        logger.info("SEARCH BY NAME DEFAULT (CONTAINS) :::: True")
                        return True
                    else:
                        return False
            else:
                if self.options.get("search_name") in name:
                    logger.info("SEARCH BY NAME DEFAULT (CONTAINS) :::: True")
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
                        logger.info("SEARCH SIZE OPTION GREATER::: True")
                        return True
                    else:
                        return False
                elif self.options.get("search_size_options") == "Smaller":
                    if search_result.get_size() <= int(self.options.get("search_size")):
                        logger.info("SEARCH SIZE OPTION SMALLER ::: True")
                        return True
                    else:
                        return False
                else:
                    if search_result.get_size() == int(self.options.get("search_size")):
                        logger.info("SEARCH SIZE OPTION EQUAL ::: True")
                        return True
                    else:
                        return False
            else:
                if search_result.get_size() == int(self.options.get("search_size")):
                    logger.info("SEARCH SIZE OPTION DEFAULT (EQUAL) ::: True")
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
                    if get_datetime(search_result.get_cdate())  > get_datetime(self.options.get("search_date")):
                        logger.info("SEARCH CREATION DATE GREATER ::: True")
                        return True
                    else:
                        return False
                elif "Smaller" in self.options:
                    if get_datetime(search_result.get_cdate()) < get_datetime(self.options.get("search_date")):
                        logger.info("SEARCH CREATION DATE SMALLER ::: True")
                        return True
                    else:
                        return False
                else:
                    if get_datetime(search_result.get_cdate()) == get_datetime(self.options.get("search_date")):
                        logger.info("SEARCH CREATION DATE EQUAL ::: True")
                        return True
                    else:
                        return False
            else:
                if get_datetime(search_result.get_cdate()) == get_datetime(self.options.get("search_date")):
                    logger.info("SEARCH CREATION DATE BY DEFAULT (EQUAL)::: True")
                    return True
                else:
                    return False
        else:
            return True

    """Allows to search by extension/filetype any file"""
    def search_by_extension(self, result):
        search_result = result
        if "search_by_extension" in self.options.keys():
            if self.options.get("search_by_extension") in search_result.get_type():
                logger.info("SEARCH EXTENSION ::: True")
                return True
            else:
                return False
        else:
            return True
