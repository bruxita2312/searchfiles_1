import os

class MyFile:

    def __init__(self, name, path, abspath, size, cdate, type):
        self.name = name
        self.type = type
        self.size=size
        self.path = path
        self.abspath = abspath
        self.cdate = cdate