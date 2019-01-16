import re
import datetime


class Validations:
    """class to validate data"""

    def is_empty(self, items):
        for item in items:
            if bool(item) is False:
                return True
        return False

    def is_whitespace(self, items):
        for item in items:
            if item.isspace() is True:
                return True
        return False

    def is_string(self, items):
        for item in items:
            if type(item) != str:
                return False
        return True

    def is_integer(self, items):
        for item in items:
            if type(item) != int:
                return False
        return True

    def is_valid_date(self, date):
        date_obj = datetime.date.today()
        date = date_obj.strftime("%d-%m-%Y")
        if date:
            return True
        else:
            return False

    def is_future_date(self, date):
        if date < datetime.date.today():
            return False
        else:
            return True

    @staticmethod
    def is_valid_email(email):
        email = email.lower()
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            res = False
        else:
            res = True
        return res

    @staticmethod
    def is_valid_password(password):
        if (len(password) < 6) is True:
            res = True
        else:
            res = False
        return res
