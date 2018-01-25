import os


class MyFolder:
    def __init__(self, name, path, abspath, size, cdate, files):
        self.name = name
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate
        self.file = []
