from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
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
                        #logger.info("FILE :::: %s \t || %s \t || %d \t || %s \t || %s \t || %s" % (result.get_name(), result.get_type(), result.get_size(), result.get_cdate(), result.get_ftype(), result.get_abspath()))
                        results.append(result)
#             for fil in folders:
#                 result = SearchResult()
#                 search_path = path.join(search_path, fil)
#                 result.set_name(fil)
#                 result.set_path(search_path)
#                 #result.set_size(int(path.getsize(search_path)))
#                 #result.set_cdate(path.getctime(search_path))
#                 #logger.info("FOLDER :::: %s \t || %s \t || %d \t || %s" %(result.get_name(), result.get_path(),result.get_size(),result.get_cdate()))
#                 add_to_list = self.add_to_results(result)
# #77962485
#                 if add_to_list == True:
#                     result.set_ftype("folder")
#                     #result.set_abspath(path.abspath(search_path))
#                     results.append(result)
        logger.info("SEARCHING RESULT TOTAL ::: %d" % int(len(results)))
        logger.info("SEARCHING end")
        return results

    def add_to_results(self, result):
        logger.info("BEGIN ADD_TO_RESULTS")
        boolean_name = self.search_by_name(result)
        #boolean_size = self.search_by_size(result)
        boolean_size = True
        #boolean_ext = self.search_by_extension(result)
        boolean_ext=True
        #boolean_ctime = self.search_by_date(result)
        boolean_ctime = True
        if boolean_name == True:
            logger.info("END OF ADD_TO_RESULTS ::::::: TRUE")
            return True
        else:
            logger.info("END OF ADD_TO_RESULTS ::::::: FALSE")
            return False

    """This method allows to make search by name"""
    def search_by_name(self, search_result):
        logger.info("BEGIN SEARCH_BY_NAME")
        logger.info("PATH TO SEARCH:::::::: %s " % self.options["search_path"])
        logger.info("NAME TO SEARCH:::::::: %s " % self.options["search_name"])
        #logger.info("ADDON TO SEARCH:::::::: %s " % self.options["search_name_options"])
        logger.info("RESULT::::: NAME :::::::: %s " % search_result.get_name())
        logger.info("RESULT::::: PATH :::::::: %s " % search_result.get_path())
        name = get_filename(search_result.get_name(),search_result.get_type())
        logger.info("RESULT::::: NAME :::::::: %s " % name)
        if "search_name" in self.options.keys():
            logger.info("There is search_name into options")
            if "search_name_options" in self.options.keys():
                if self.options.get("search_name_options") == "Exact":
                    if self.options.get("search_name") == name:
                        logger.info("1 EXACT >>>> YESSSSS")
                        return True
                    else:
                        logger.info("2 EXACT >>>> NOOOOOOO")
                        return False
                elif self.options.get("search_name_options") == "Contains":
                    if self.options.get("search_name") in name:
                        logger.info("1 CONTAINS >>>> YESSSS")
                        return True
                    else:
                        logger.info("2 CONTAINS >>>> NOOOOOO")
                        return False
                else:
                    if self.options.get("search_name") in name:
                        logger.info("3 CONTAINS >>>> YESSSS")
                        return True
                    else:
                        logger.info("4 CONTAINS >>>> NOOOOOO")
                        return False
            else:
                if self.options.get("search_name") in name:
                    logger.info("5 CONTAINS >>>> YESSSS")
                    return True
                else:
                    logger.info("6 CONTAINS >>>> NOOOOOO")
                    return False
        else:
            logger.info("There is not search_name into options")
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


class SearchBasic(object):

    def __init__(self):
        pass

    def options(self, option, text=None, spath="/"):
        logger.info("PATH ::: %s" % spath)
        logger.info("Text to search ::: %s" % text)
        if (option == 1):
            self._search_file_by_name(text, spath)
        elif (option == 2):
            self._search_by_size(text, spath)
        elif (option == 3):
            #self._search_folder_by_name(text, spath)
            pass
        else:
            print("Exiting from searcher")
            logger.info("Exit from basic search")
            exit(0)

    def _search_file_by_name(self, text, spath):
        logger.info("Searching files naming %s" % text)
        results = []
        for search_path, folders, files in walk(spath):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if str.lower(text) in str.lower(fil):
                    logger.info("FILE::: %s " % (fil))
                    rfile = SearchResult()
                    rfile.set_name(fil)
                    rfile.set_path(search_path)
                    rfile.set_size(int(path.getsize(fil_search_path)))
                    rfile.set_abspath(path.abspath(fil_search_path))
                    create_date = timestamp_to_date(path.getctime(fil_search_path))
                    rfile.set_cdate(create_date)
                    rfile.set_ftype("file")
                    #print ("%s \t || %s \t || %d \t || %s" %(rfile.get_name(), rfile.get_path(),rfile.get_size(),rfile.get_cdate()))
                    #print(" "+rfile.get_name()+"\t   || \t   "+rfile.get_path())
                    results.append(rfile)
            for fol in folders:
                fol_search_path = path.join(search_path, fol)
                #print("FOLDER::: %s :: %s " % (fol, fol_search_path))
                if str.lower(text) in str.lower(fol):
                    logger.info("FOLDER::: %s " % (fol))
                    rfile = SearchResult()
                    rfile.set_name(fol)
                    rfile.set_path(search_path)
                    rfile.set_size(int(path.getsize(fol_search_path)))
                    rfile.set_abspath(path.abspath(fol_search_path))
                    create_date = timestamp_to_date(path.getctime(fil_search_path))
                    rfile.set_cdate(create_date)
                    rfile.set_ftype("folder")
                    print(" "+fol+"            FOLDER           "+search_path)
                    results.append(rfile)
        logger.info("-----------------------------------------------")
        logger.info("TOTAL RESULTS OF FILES ::: %d  " % len(results))
        logger.info("===============================================================================")
        matches= str(len(results))
        print("******* Total items matched: " + matches + " *******")



        return results

    def _search_by_ext(self, text, spath):
        logger.info("Searching files with extension %s" % text)
        results = []
        for search_path, folders, files in walk(spath):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                ext = get_extension(fil_search_path)
                name = get_name(fil_search_path)
                #print("NAME:::: %s            TYPE::::%s" % (name,ext))

                if text in ext:
                    logger.info("FILE ::: %s " % fil_search_path)
                    print("  "+fil+"                    "+search_path)
                    rfile = SearchResult()
                    rfile.set_name(fil)
                    rfile.set_path(search_path)
                    rfile.set_size(int(path.getsize(fil_search_path)))
                    rfile.set_abspath(path.abspath(fil_search_path))
                    create_date = timestamp_to_date(path.getctime(fil_search_path))
                    rfile.set_cdate(create_date)
                    rfile.set_ftype("file")
                    results.append(rfile)
        logger.info("-----------------------------------------------")
        logger.info("TOTAL RESULTS OF FILES ::: %d  " % len(results))
        logger.info("===============================================================================")
        matches = str(len(results))
        print("")
        print("")
        print("******* Total items matched: " + matches+" *******")

        return results

    def _search_by_size(self, text, spath):
        logger.info("Searching files with size %d" % int(text))
        results = []
        xfile_size= size_converter_to_bytes(int(text), "mb")
        print ("SIZE TO SEARCH ::: %d " % xfile_size)
        for search_path, folders, files in walk(spath):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if int(path.getsize(fil_search_path)) > xfile_size:
                    c= size_converter(path.getsize(fil_search_path),"mb")
                    logger.info("FILE::: %s  ::::: SIZE::::: %d" % (fil_search_path, c))
                    print("Item"+fil_search_path+" "+c)
                    rfile = SearchResult()
                    rfile.set_name(fil)
                    rfile.set_path(search_path)
                    rfile.set_size(int(path.getsize(fil_search_path)))
                    rfile.set_abspath(path.abspath(fil_search_path))
                    create_date = timestamp_to_date(path.getctime(fil_search_path))
                    rfile.set_cdate(create_date)
                    rfile.set_ftype("file")
                    results.append(rfile)
        logger.info("-----------------------------------------------")
        logger.info("TOTAL RESULTS OF FILES ::: %d  " % len(results))
        logger.info("===============================================================================")
        print(" ")
        return results


if __name__ == "__main__":
    # search = SearchBasic()
    # search.options(1, "sales", "f:\\")
    # search.options(3, "one", "f:\\")
    # search.options(2, 9968, "f:\\")
    # search.options(4)

    options = {"search_path":"d:/", "search_on":"file","search_name":"menu"}
    options2 = {"search_path": "d:/", "search_on": "file", "search_name": "menu","search_size": 1037}
    options3 = {"search_path": "d:/", "search_on": "file", "search_name": "menu", "search_size": 1500,"size_is":"greater"}
    searcha = Search()
    searcha.set_options(options)
    searcha.searching()
    searcha.set_options(options3)
    searcha.searching()
