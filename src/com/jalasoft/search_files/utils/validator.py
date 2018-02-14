import os
from src.com.jalasoft.search_files.utils.logging import logger

class Validator:
    def is_only_numbers(self, value):

        if type(value) != int:
            logger.error("Failed Verification, the type must be a option validddddd: ".format(value))

    def is_menu(self, menu, limit):
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
        if type(value) != int:
            logger.error("Failed Verification, the type must be a number: ".format(value))

    def is_only_text(self, value):
        if type(value) not in (int, float, complex):
            logger.error("Failed Verification, only a text value should be insert:".format(value))

    def empty_validation(self, value):
        if value is None:
            logger.error("Empty value found.")

    def is_path(self, value, intentos=0):
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
        pass

    def response_status(self, response_dict):
        status = "Pass"
        for response in response_dict.keys():
            if response_dict[response]['status'] == "Fail":
                status = "Fail, response status"
        return status

if __name__ == "__main__":
    path1 = 'C:\\Users'
    validator = Validator()