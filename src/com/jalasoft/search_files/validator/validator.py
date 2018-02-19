import os
import os.path as path
from src.com.jalasoft.search_files.utils.logging import logger

"""This class contain methods that will help to validate inputs
"""


class Validator:
    def __init__(self):
        pass

    def is_menu(self, menu, limit):
        """This method verify that the option entered is a valid option of the menu """
        """:return: Boolean"""
        res_menu_validator = False

        if self.is_only_numbers(self, menu):
            if limit >= menu >= 1:
                res_menu_validator = True
            else:
                res_menu_validator = False
        else:
            res_menu_validator = False
        return res_menu_validator

    def is_only_numbers(self, value):
        """This method verify that the value is a numeric value """
        """:return: Boolean"""
        if type(value) != int:
            logger.error("Failed Verification, the type must be a option valid: ".format(value))

    def is_only_text(self, value):
        """This method verify that the value is a text value """
        """:return: Boolean"""
        if type(value) not in (int, float, complex):
            logger.error("Failed Verification, only a text value should be insert:".format(value))

    def empty_validation(self, value):
        """This method verify that the value is a empty value """
        """:return: Boolean"""
        if value is None:
            logger.error("Empty value found.")

    def is_path(self, value, intentos=0):
        """This method verify that the path is valid """
        """:return: Boolean"""
        res_path = False
        while intentos < 5:
            if os.path.lexists(value) == True:
                res_path = True
                break
            else:
                res_path = False
                intentos += 1
        if intentos >= 5:
            logger.error("Incorrect Path, try " + str(intentos) + " attempts")
        return res_path

    def is_file(self, value, intentos=0):
        """This method verify that the path is a directory"""
        """:return: Boolean"""
        res_file = False
        if path.isfile(value):
            extension = path.splitext(value)[1]
            if extension is None:
                res_file = True
            else:
                res_file = False
                logger.error("The object is not a directory".format(path))
        return res_file


if __name__ == "__main__":
    path3 = 'C:\\Users'

    validator = Validator()
    # print(validator.is_path(path3, 3))
