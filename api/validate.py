class Validation:
    def if_empty_string_is_passed(self,user_input):
        if str(user_input).replace(" ", "") == "":
            return True
        return False  

    