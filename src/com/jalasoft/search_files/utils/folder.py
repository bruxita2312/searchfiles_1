class MyFolder(object):
    def __init__(self, name, path, abspath, size, cdate):
        self.name = name
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate
        self.files = []

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_path(self):
        return self.path

    def get_abspath(self):
        return self.abspath

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size

    def set_path(self, path):
        self.path = path

    def set_abspath(self, abspath):
        self.abspath = abspath

    def set_files(self, files):
        self.files=files