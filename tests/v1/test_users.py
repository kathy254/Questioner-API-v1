import json
import datetime

from .base_tests import BaseTest
from app.api.v1.models.user_models import Members

signup_url = "api/v1/users/signup"

class TestUser(BaseTest):

    def test_signup(self):
        with self.client:
            signup_payload = {
                "first_name": "cath",
                "last_name": "faithe",
                "other_name": "None",
                "email": "me345@gmail.com",
                "phone_number": "0303030",
                "username": "ididiiu",
                "password": "idididi"
            }
            response = self.client.post(signup_url, data=json.dumps(signup_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))
            
            self.assertEqual(result["status"], 201)
            self.assertEqual(result["response"], "User with username ididiiu was added successfully")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")

    def test_existing_username(self):

        with self.client:
            #register user

            register1 = {
                "first_name": "cat",
                "last_name": "faith",
                "other_name": "Noone",
                "email": "me@gmail.com",
                "phone_number": "0303030",
                "username": "idid",
                "password": "idididi"
            }
            self.client.post(signup_url, data = json.dumps(register1), content_type = "application/json")

            #register with existing username
            new_user = {
                "first_name": "cat",
                "last_name": "faith",
                "other_name": "Noone",
                "email": "me2@gmail.com",
                "phone_number": "0303030",
                "username": "idid",
                "password": "idididi"
            }
            response2 = self.client.post(signup_url, data = json.dumps(new_user), content_type = "application/json")
            result3 = json.loads(response2.data.decode("UTF-8"))

            self.assertEqual(result3["status"], 500)
            self.assertEqual(result3["message"], "This username already exists")
            self.assertEqual(response2.status_code, 500)
            self.assertTrue(response2.content_type == "application/json")


    

    def test_existing_email(self):
        with self.client:
            #register a user
            payload = {
                "first_name": "cat",
                "last_name": "faith",
                "other_name": "Noone",
                "email": "me@gmail.com",
                "phone_number": "0303030",
                "username": "idid",
                "password": "idididi"
            }

            self.client.post(signup_url, data = json.dumps(payload), content_type = "application/json")

            #register user with existing email
            payload3 = {
                "first_name": "not",
                "last_name": "name",
                "other_name": "dontknow",
                "email": "me@gmail.com",
                "phone_number": "003030303",
                "username": "myusername",
                "password": "idididi"
            }
            register3 = self.client.post(signup_url, data = json.dumps(payload3), content_type = "application/json")
            result = json.loads(register3.data.decode("UTF-8"))
            self.assertEqual(result["status"], 500)
            self.assertEqual(result["message"], "This email address already exists. Please log in")
            self.assertEqual(register3.status_code, 500)
            self.assertTrue(register3.content_type == "application/json")