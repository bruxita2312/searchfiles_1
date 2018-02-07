from src.com.jalasoft.search_files.utils.search_result import SearchResult
from src.com.jalasoft.search_files.utils.search_util import *
from src.com.jalasoft.search_files.utils.logging import logger
from os import listdir, walk, getcwd, path
import datetime


class SearchAdvance(object):

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

    def search_options(self):
        logger.info("SEARCH_OPTIONS begin")
        try:
            if self.options.get("type") == "basic":
                logger.info("BASIC SEARCH:::")
                # self.set_search_results(self.basic_search(self.options))
            else:
                logger.info("ADVANCED SEARCH:::")
                # self.set_search_results(self.adv_search(self.options))
        except:
            pass
        logger.info("SEARCH_OPTIONS end")

    def searching(self):
        logger.info("==========================================\n=====================================")
        logger.info("=================================\n==============================================")
        logger.info("SEARCHING begin")
        results = []
        if "search_path" not in self.options.keys():
            self.options["search_path"] = "/"
        logger.info("\n Received options: \n%s" % self.options.keys())
        logger.info("\n Received values: \n%s" % self.options.items())
        spath = self.options.get("search_path")
        logger.info("PATH :: %s" % spath)
        for search_path, folders, files in walk(spath):
            if "search_on" in self.options.keys():
                if self.options.get("search_on") == "file" or self.options.get("search_on") == "both":
                    for fil in files:
                        result = SearchResult()
                        fil_path = path.join(search_path, fil)
                        result.set_name(fil)
                        result.set_path(search_path)
                        result.set_type(get_extension(fil_path))
                        result.set_ftype("file")
                        result.set_size(path.getsize(fil_path))
                        #result.set_abspath(path.abspath(fil_path))
                        result.set_cdate(timestamp_to_date(path.getctime(fil_path)))
                        by_name = self.search_by_name(result)
                        by_size = self.search_by_size(result)
                        by_ext = self.search_by_extension(result)
                        if by_name == True and by_size == True and by_ext== True:
                            logger.info("FILE::: %s :: %s :: %d :: %s" % (result.get_name(), result.get_path(), result.get_size(), result.get_cdate()))
                            results.append(result)
                if self.options.get("search_on") == "folder" or self.options.get("search_on") == "both":
                    for fil in folders:
                        result = SearchResult()
                        fil_path = path.join(search_path, fil)
                        result.set_name(fil)
                        result.set_path(fil_path)
                        result.set_ftype("folder")
                        result.set_size(path.getsize(fil_path))
                        #result.set_abspath(path.abspath(fil_path))
                        result.set_cdate(timestamp_to_date(path.getctime(fil_path)))
                        by_name = self.search_by_name(result)
                        by_size = self.search_by_size(result)
                        by_ext = self.search_by_extension(result)
                        if by_name == True and by_size == True and by_ext == True:
                            logger.info("FILE::: %s :: %s :: %d :: %s" % (result.get_name(), result.get_path(), result.get_size(), result.get_cdate()))
                            results.append(result)
        logger.info("-----------------------------------------------")
        logger.info("TOTAL RESULTS OF FILES ::: %d  " % len(results))
        logger.info("SEARCHING end")
        logger.info("=====================================\n==========================================")
        return results

    def search_on(self, result):
        search_result = result
        name = get_name(search_result.get_name())
        if "search_on" in self.options.keys():
            if self.options.get("search_on") == result.get_ftype():
                pass
            if self.options.get("name") in name:
                return True
            else:
                return False
        else:
            return True

    def search_by_name(self, result):
        search_result = result
        #name = get_name(search_result.get_name())
        name = search_result.get_name()
        if "search_name" in self.options.keys():
            if self.options.get("search_name") in name:
                return True
            else:
                return False
        else:
            return True

    def search_by_size(self, result):
        search_result = result
        if "search_size" in self.options.keys():
            asearch_size = size_converter_to_bytes(self.options.get("search_size"),"mb")
            if "size_is" in self.options.keys():
                if self.options.get("size_is") == "greater":
                    if search_result.get_size() > asearch_size:
                        return True
                    else:
                        return False
                elif self.options.get("size_is") == "smaller":
                    if search_result.get_size() < asearch_size:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if search_result.get_size() == asearch_size:
                    return True
                else:
                    False
        else:
            return True

    def search_by_date(self, result):
        search_result = result
        if "date" in self.options.keys():
            if "greater" in self.options.keys():
                if search_result.get_ctime() > self.options.get("date"):
                    return True
                else:
                    False
            elif "less" in self.options.keys():
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

    def search_by_extension(self, result):
        search_result = result
        if "type" in self.options.keys():
            if self.options.get("type") in search_result.get_ftype():
                return True
            else:
                False
        else:
            return True


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
            self._search_folder_by_name(text, spath)
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
                    results.append(rfile)
        logger.info("-----------------------------------------------")
        logger.info("TOTAL RESULTS OF FILES ::: %d  " % len(results))
        logger.info("===============================================================================")
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
        return results

    def _search_by_size(self, text, spath):
        logger.info("Searching files with size %d" % int(text))
        results = []
        xfile_size= size_converter_to_bytes(int(text), "mb")
        print ("SIZE TO SEARCH ::: %d " % xfile_size)
        for search_path, folders, files in walk(spath):
            for fil in files:
                fil_search_path = path.join(search_path, fil)
                if int(path.getsize(fil_search_path)) >= xfile_size:
                    c= size_converter(path.getsize(fil_search_path),"mb")
                    logger.info("FILE::: %s  ::::: SIZE::::: %d" % (fil_search_path, c))
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
        return results


if __name__ == "__main__":
    # search = SearchBasic()
    # search.options(1, "sales", getcwd())
    # search.options(3, "one", getcwd())
    # search.options(2, 9968, getcwd())
    # search.options(4)

    options = {"search_path":"f:/", "search_on":"file","search_name":"menu"}
    options2 = {"search_path": "f:/", "search_on": "file", "search_name": "menu","search_size": 1037}
    options3 = {"search_path": "f:/", "search_on": "file", "search_name": "menu", "search_size": 1500,"size_is":"greater"}
    searcha = SearchAdvance()
    searcha.set_options(options)
    searcha.searching()
    searcha.set_options(options3)
    searcha.searching()
