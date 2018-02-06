import logging.config
import os

logging.basicConfig(filename="../../../../../log/validator.log", level=logging.DEBUG,
                    format='%(levelname)s : %(asctime)s : %(message)s')
from concurrent.futures._base import LOGGER


class Validator:
    def __init__(self):
        pass

    def is_menu(self, menu, limit):
        res_menu_validator = False

        if is_only_numbers(self, menu):
            if limit >= menu >= 1:
                res_menu_validator = True
            else:
                res_menu_validator = False
        else:
            res_menu_validator = False
        return res_menu_validator

    def is_only_numbers(self, value):
        if type(value) != int:
            LOGGER.error("Failed Verification, the type must be a option valid: ".format(value))

    def is_only_text(self, value):
        if type(value) not in (int, float, complex):
            LOGGER.error("Failed Verification, only a text value should be insert:".format(value))

    def empty_validation(self, value):
        if value is None:
            LOGGER.error("Empty value found.")

    def is_path(self, value, intentos=0):
        while intentos < 5:
            if os.path.lexists(value) == True:
                res_path = True
                break
            else:
                res_path = False
                intentos += 1
        if intentos >= 5:
                    LOGGER.error("Incorrect Path, try " + str(intentos) + " attempts")
        return res_path

    def is_file(self, value, intentos=0):
        {}

    def response_status(self, response_dict):
        status = "Pass"
        for response in response_dict.keys():
            if response_dict[response]['status'] == "Fail":
                status = "Fail"
        return status

