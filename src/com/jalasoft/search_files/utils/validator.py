class Validator:

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
        {}

    def is_only_text(self, value):
        {}

    def is_alphanumeric(self, value):
        {}

    def empty_validation(self, value):
        {}

    def response_status(self, response_dict):
        status = "Pass"
        for response in response_dict.keys():
            if response_dict[response]['status'] == "Fail":
                status = "Fail"
        return status