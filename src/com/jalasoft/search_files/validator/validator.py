import os
import os.path as path
from src.com.jalasoft.search_files.utils.logging import logger

class Validator:
    def __init__(self):
        pass

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
            logger.error("Failed Verification, the type must be a option valid: ".format(value))

    def is_only_text(self, value):
        if type(value) not in (int, float, complex):
            logger.error("Failed Verification, only a text value should be insert:".format(value))

    def empty_validation(self, value):
        if value is None:
            logger.error("Empty value found.")

    def is_path(self, value, intentos=0):
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
        res_file =False
        if path.isfile(value):
            extension = path.splitext(value)[1]
            if extension is None:
                res_file = True
            else:
                res_file = False
                logger.error("The object is not a directory".format(path))
        return res_file


def response_status(self, response_dict):
    status = "Pass"
    for response in response_dict.keys():
        if response_dict[response]['status'] == "Fail":
            status = "Fail"
    return status


if __name__ == "__main__":
    # path3 = 'D:\\10. Desk degamboa\desk28072017\\31bb37f3-31b6-430b-8b7f-ee16517ae58e_1.521b6181d1cc5f3acc5ea330125c3e8e.jpeg'
    path3 = 'C:\\Users'
    path5 = ''
    path0 = "D:\\10. Desk degamboa\\03102016 desktop's files"

    validator = Validator()

    #print(validator.is_path(path3, 4))
    #print(validator.is_path(path5))

    # print(validator.is_menu())
    # print(validator.is_only_numbers())
    # print(validator.is_only_text())
    # print(validator.empty_validation())
    # print(validator.is_file(path5, 4))
    # print(validator.is_file())