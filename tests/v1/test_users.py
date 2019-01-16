import json
import datetime

from .base_tests import BaseTest
from app.api.v1.models.user_models import Members

signup_url = "api/v1/users/signup"
login_url = "api/v1/users/login"


class TestUser(BaseTest):

    def setUp(self):
        super().setUp()
        self.signup_payload = {"first_name": "catherine", "last_name": "faith", "other_name": "Were",
                               "email": "me345@gmail.com", "phone_number": "0303030", "username": "cathy",
                               "password": "mypass"
                               }

        self.whitespace_payload = {"first_name": " ", "last_name": "faith", "other_name": "Were",
                                   "email": "me345@gmail.com", "phone_number": "0303030",
                                   "username": "cathy", "password": "mypass"
                                   }

        self.invalid_email = {"first_name": "catherine", "last_name": "faith", "other_name": "Were",
                              "email": "me345.com", "phone_number": "0303030", "username": "cathy",
                              "password": "mypass"
                              }

        self.invalid_password = {"first_name": "catherine", "last_name": "faith",
                                 "other_name": "Were", "email": "me345@gmail.com",
                                 "phone_number": "0303030", "username": "cathy", "password": "me"
                                 }

    def tearDown(self):
        super().tearDown()
        self.signup_payload = None
        self.whitespace_payload = None
        self.invalid_email = None
        self.invalid_password = None

    def test_signup(self):
        response = self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["response"], "User with username cathy was added successfully")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.content_type == "application/json")

    def test_empty_data(self):
        response1 = self.client.post(signup_url, data=json.dumps(""), content_type="application/json")
        result1 = json.loads(response1.data.decode("UTF-8"))

        self.assertEqual(result1["message"], "Please fill out all the fields")
        self.assertEqual(response1.status_code, 406)
        self.assertTrue(response1.content_type == "application/json")

    def test_whitespace_data(self):
        response1 = self.client.post(signup_url, data=json.dumps(self.whitespace_payload), content_type="application/json")
        result1 = json.loads(response1.data.decode("UTF-8"))

        self.assertEqual(result1["message"], "Data cannot contain whitespaces only")
        self.assertEqual(response1.status_code, 406)
        self.assertTrue(response1.content_type == "application/json")

    def test_incorrect_email(self):
        response1 = self.client.post(signup_url, data=json.dumps(self.invalid_email), content_type="application/json")
        result1 = json.loads(response1.data.decode("UTF-8"))

        self.assertEqual(result1["message"], "Please enter a valid email address")
        self.assertEqual(response1.status_code, 406)
        self.assertTrue(response1.content_type == "application/json")

    def test_incorrect_password(self):
        response1 = self.client.post(signup_url, data=json.dumps(self.invalid_password), content_type="application/json")
        result1 = json.loads(response1.data.decode("UTF-8"))

        self.assertEqual(result1["message"], "Password should be at least 6 characters long")
        self.assertEqual(response1.status_code, 406)
        self.assertTrue(response1.content_type == "application/json")

    def test_existing_username(self):
        self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")

        new_user = {
            "first_name": "cat",
            "last_name": "faith",
            "other_name": "Noone",
            "email": "me2@gmail.com",
            "phone_number": "0303030",
            "username": "cathy",
            "password": "secret"
        }
        response2 = self.client.post(signup_url, data=json.dumps(new_user), content_type="application/json")
        result3 = json.loads(response2.data.decode("UTF-8"))

        self.assertEqual(result3["status"], 500)
        self.assertEqual(result3["message"], "This username already exists. Please choose another one.")
        self.assertEqual(response2.status_code, 500)
        self.assertTrue(response2.content_type == "application/json")

    def test_existing_email(self):

        self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")

        payload3 = {
            "first_name": "not",
            "last_name": "name",
            "other_name": "dontknow",
            "email": "me345@gmail.com",
            "phone_number": "003030303",
            "username": "myusername",
            "password": "idididi"
        }
        register3 = self.client.post(signup_url, data=json.dumps(payload3), content_type="application/json")
        result = json.loads(register3.data.decode("UTF-8"))
        self.assertEqual(result["status"], 500)
        self.assertEqual(result["message"], "This email address already exists. Please log in")
        self.assertEqual(register3.status_code, 500)
        self.assertTrue(register3.content_type == "application/json")

    def test_user_login(self):

        self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")

        login_payload = {"username": "cathy", "password": "mypass"}
        response4 = self.client.post(login_url, data=json.dumps(login_payload), content_type="application/json")
        result4 = json.loads(response4.data.decode("UTF-8"))

        self.assertEqual(result4["status"], 201)
        self.assertEqual(result4["message"], "You have successfully logged in.")
        self.assertEqual(response4.status_code, 201)
        self.assertTrue(response4.content_type == "application/json")

    def test_incorrect_username(self):
        self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")

        incorrect_payload = {"username": "faith", "password": "faithuser"}
        response5 = self.client.post(login_url, data=json.dumps(incorrect_payload), content_type="application/json")
        result5 = json.loads(response5.data.decode("UTF-8"))

        self.assertEqual(result5["status"], 404)
        self.assertEqual(result5["message"], "User does not exist")
        self.assertEqual(response5.status_code, 404)
        self.assertTrue(response5.content_type == "application/json")

    def test_wrong_login_password(self):
        self.client.post(signup_url, data=json.dumps(self.signup_payload), content_type="application/json")

        incorrect_password = {"username": "cathy", "password": "notsure"}
        response6 = self.client.post(login_url, data=json.dumps(incorrect_password), content_type="application/json")
        result6 = json.loads(response6.data.decode("UTF-8"))

        self.assertEqual(result6["status"], 400)
        self.assertEqual(result6["message"], "Password is incorrect.")
        self.assertEqual(response6.status_code, 400)
        self.assertTrue(response6.content_type == "application/json")
