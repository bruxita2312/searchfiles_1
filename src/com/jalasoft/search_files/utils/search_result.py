
class SearchResult(object):

    def __init__(self):
        self.name = ""
        self.type = ""
        self.ftype = ""
        self.size=0
        self.path = ""
        self.abspath = ""
        self.cdate = ""

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_ftype(self):
        return self.ftype

    def get_size(self):
        return self.size

    def get_path(self):
        return self.path

    def get_abspath(self):
        return self.abspath

    def get_cdate(self):
        return self.cdate

    def set_name(self, name):
        self.name=name

    def set_type(self, type):
        self.type=type

    def set_ftype(self, ftype):
        self.ftype=ftype

    def set_size(self, size):
        self.size=size

    def set_path(self,path):
        self.path=path

    def set_abspath(self, abspath):
        self.abspath = abspath

    def set_cdate(self, cdate):
        self.cdate=cdate
