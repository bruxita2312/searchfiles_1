class MyFolder:
    def __init__(self, name, path, abspath, size, cdate):
        self.name = name
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate
        self.files = []

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