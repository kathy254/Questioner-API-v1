import datetime
from ...v1.utils.validations import Validations

user_accounts = []
user_id = 1


class Members(Validations):
    """A class to represent the user model"""

    def create_account(self, first_name, last_name, other_name, email, phone_number, username, password, registered, isAdmin):
        """method to add new user to user_accounts list"""
        new_user = dict(
            user_id=len(user_accounts) + 1,
            first_name=first_name,
            last_name=last_name,
            other_name=other_name,
            email=email,
            phone_number=phone_number,
            username=username,
            password=password,
            registered=datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            isAdmin=False
        )

        payload = first_name, last_name, other_name, email, phone_number, username, password

        if self.is_empty(payload) is True:
            res = {"message": "Please fill out all the fields"}, 406
        elif self.is_whitespace(payload) is True:
            res = {"message": "Data cannot contain whitespaces only"}, 406
        elif self.is_valid_email(email) is False:
            res = {"message": "Please enter a valid email address"}, 406
        elif self.is_valid_password(password) is True:
            res = {"message": "Password should be at least 6 characters long"}, 406
        else:
            res = user_accounts.append(new_user)
            res = {
                        "status": 201,
                        "response": "User with username {} was added successfully".format(username),
                        "data": new_user
                    }, 201
        return res

    @staticmethod
    def get_user_email(email):
        email_exists = [user for user in user_accounts if user["email"] == email]
        if email_exists:
            res = True
        else:
            res = False
        return res

    @staticmethod
    def get_user_username(username):
        single_user = [user for user in user_accounts if user["username"] == username]
        if single_user:
            res = single_user[0]
        else:
            res = False
        return res

    @staticmethod
    def get_user_by_id(user_id):
        single_id = [user for user in user_accounts if user["user_id"] == user_id]
        if single_id:
            res = single_id[0]
        else:
            res = False
        return res
