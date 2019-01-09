import datetime
from ...v1.utils.validations import Validations

user_accounts = []
user_id = 1

class Members(Validations):
    """A class to represent the user model"""

    def create_account(self, first_name, last_name, other_name, email, phone_number, username, password, registered, isAdmin):
        """method to add new user to user_accounts list"""
        new_user = dict(
            user_id = len(user_accounts) + 1,
            first_name = first_name,
            last_name =last_name,
            other_name = other_name,
            email = email,
            phone_number = phone_number,
            username = username,
            password = password,
            registered = datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            isAdmin = False
        )

        user_accounts.append(new_user)
        return new_user

    @staticmethod
    def get_user_email(email):
        email_exists = [user for user in user_accounts if user["email"] == email]
        if email_exists:
            return "This email address already exists. Please log in"
        else:
            return "User not found"

    @staticmethod
    def get_user_username(username):
        single_user = [user for user in user_accounts if user["username"] == username]
        if single_user:
            return single_user[0]
        else:
            return "User not found"

    @staticmethod
    def get_user_by_id(user_id):
        single_id = [user for user in user_accounts if user["user_id"] == user_id]
        if single_id:
            return single_id[0]
        else:
            return "User not found"