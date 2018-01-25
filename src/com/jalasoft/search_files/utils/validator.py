class Validator:


def menu_validator(menu):
    res_menu_validator = False

    if is_only_numbers(menu):

        if 4 >= menu >= 1:
            res_menu_validator = True
        else:
            res_menu_validator = False
    else:
        res_menu_validator = False
    return res_menu_validator

def is_only_numbers(input):
    {}

def is_only_text(input):
    {}

def is_alphanumeric(input):
    {}

def empty_validation(input):
    {}
