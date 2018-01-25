class MyFile:

    def __init__(self, name, path, abspath, size, cdate, type):
        self.name = name
        self.type = type
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate

    def set_name(self, name):
        self.name=name

    def set_type(self, type):
        self.type=type

    def set_size(self,size):
        self.size=size

    def set_path(self,path):
        self.path=path

    def set_abspath(self, abspath):
        self.abspath = abspath