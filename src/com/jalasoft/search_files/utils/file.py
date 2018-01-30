class MyFile(object):

    def __init__(self, name, path, abspath, size, cdate, type):
        self.name = name
        self.type = type
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_size(self):
        return self.size

    def get_path(self):
        return self.path

    def get_abspath(self):
        return self.abspath

    def set_name(self):
        self.name

    def set_type(self):
        self.type

    def set_size(self):
        self.size

    def set_path(self,path):
        self.path=path

    def set_abspath(self, abspath):
        self.abspath = abspath