"""Stores the info of any file or folder returned by searcher"""


class SearchResult(object):

    def __init__(self):
        self.name = ""
        self.type = ""
        self.ftype = ""
        self.size = 0
        self.path = ""
        self.abspath = ""
        self.cdate = ""

    def get_name(self):
        """Returns file/folder name"""
        return self.name

    def get_type(self):
        """Returns the file extension"""
        return self.type

    def get_ftype(self):
        """Returns the object type (file or folder)"""
        return self.ftype

    def get_size(self):
        """Returns the file/folder size"""
        return self.size

    def get_path(self):
        """Returns the file/folder path"""
        return self.path

    def get_abspath(self):
        """Returns the absolute file/folder path"""
        return self.abspath

    def get_cdate(self):
        """Returns the date when file/folder was created"""
        return self.cdate

    def get_mdate(self):
        """Returns the date when file/folder was modified"""
        return self.mdate

    def set_name(self, name):
        """Sets the file/folder name"""
        self.name = name

    def set_type(self, type):
        """Sets the file extension"""
        self.type = type

    def set_ftype(self, ftype):
        """Sets if the stored object type is a file or a folder"""
        self.ftype = ftype

    def set_size(self, size):
        """Sets the file/folder size"""
        self.size = size

    def set_path(self, path):
        """Sets the file/folder path"""
        self.path = path

    def set_abspath(self, abspath):
        """Sets the absolute file/folder path"""
        self.abspath = abspath

    def set_cdate(self, cdate):
        """Sets the date when file/folder was created"""
        self.cdate = cdate

    def set_mdate(self, mdate):
        """Sets the date when file/folder was modified"""
        self.mdate = mdate