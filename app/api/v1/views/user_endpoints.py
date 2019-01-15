from flask import Flask, Blueprint, json, jsonify, make_response, request
from flask_restplus import Api, fields, Namespace, Resource, reqparse

from ...v1.models import user_models

parser = reqparse.RequestParser()
parser.add_argument("first_name", help="This field cannot be blank")
parser.add_argument("last_name", help="This field cannot be blank")
parser.add_argument("other_name", help="This field cannot be blank")
parser.add_argument("email", help="This field cannot be blank")
parser.add_argument("phone_number", help="This field cannot be blank")
parser.add_argument("username", help="This field cannot be blank")
parser.add_argument("password", help="This field cannot be blank")
parser.add_argument("registered", help="This field cannot be blank")
parser.add_argument("isAdmin", help="This field cannot be blank")

qs_users = Namespace("users", description="User endpoints")

mod_register = qs_users.model("Create a new account", {
    "first_name": fields.String("Users first name"),
    "last_name": fields.String("Users last name"),
    "other_name": fields.String("Users other name"),
    "email": fields.String("Users email address"),
    "phone_number": fields.String("Users phone number"),
    "username": fields.String("Users username"),
    "password": fields.String("Users password")
})


@qs_users.route('/signup')
class RegisterUser(Resource):
    @qs_users.doc(security="apikey")
    @qs_users.expect(mod_register)
    def post(self):
        args = parser.parse_args()
        first_name = args["first_name"]
        last_name = args["last_name"]
        other_name = args["other_name"]
        email = args["email"]
        phone_number = args["phone_number"]
        username = args["username"]
        password = args["password"]
        registered = args["registered"]
        isAdmin = args["isAdmin"]

        email_found = user_models.Members().get_user_email(email)

        if email_found is False:
            if user_models.Members().get_user_username(username) is False:
                try:
                    result = user_models.Members().create_account(first_name, last_name, other_name, email, phone_number, username, password, registered, isAdmin)
                    return result

                except Exception as e:
                    return make_response(jsonify({
                        "message": str(e),
                        "status": "Failed"
                    }), 500)

            return make_response(jsonify({
                "status": 500,
                "message": "This username already exists. Please choose another one."
            }), 500)

        return make_response(jsonify({
            "status": 500,
            "message": "This email address already exists. Please log in"
        }), 500)


mod_login = qs_users.model('Log into your account', {
    "username": fields.String("username"),
    "password": fields.String("password")
    })


@qs_users.route('/login')
class Login(Resource):
    @qs_users.expect(mod_login)
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]

        try:
            present_user = user_models.Members().get_user_username(username)
            if present_user is False:
                return make_response(jsonify({
                    "status": 404,
                    "message": "User does not exist"
                }), 404)

            if present_user:
                if present_user["password"]:
                    return make_response(jsonify({
                        "status": 201,
                        "message": "You have successfully logged in."
                    }), 201)

                else:
                    return make_response(jsonify({
                        "status": 400,
                        "message": "Password is incorrect."
                    }), 400)

        except Exception as e:
            return make_response(jsonify({
                "status": 500,
                "message": str(e)
            }), 500)
