from os import listdir, walk, getcwd, path
import unittest
from src.com.jalasoft.search_files.search import *


# noinspection PyUnresolvedReferences
class SearchTest(unittest.TestCase):

    def test_search_needs_path(self):
        path = getcwd()
        search = Search(path)
        pass

    def test_search_by_name_returns_an_array(self):
        pass

    def test_search_by_name_return_xxx(self):
        pass