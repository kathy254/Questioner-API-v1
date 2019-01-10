from flask import Flask, request, jsonify, Blueprint, json, make_response
from flask_restplus import Resource, reqparse, Namespace, fields, Api

from ...v1.models import question_models

parser = reqparse.RequestParser()
parser.add_argument("createdOn", help="This field cannot be blank")
parser.add_argument("createdBy", help="This field cannot be blank")
parser.add_argument("meetup_id", help="This field is optional")
parser.add_argument("title", help="This field cannot be blank")
parser.add_argument("body", help="This field cannot be blank")
parser.add_argument("votes", help="This field cannot be blank")

qs_questions = Namespace("questions", description="Question endpoints")

mod_post_question = qs_questions.model("Post a new question", {
    "createdOn": fields.String("Date question was posted"),
    "createdBy": fields.Integer("User id of member who posted it"),
    "meetup_id": fields.Integer("ID of meetup where the question is posted"),
    "title": fields.String("Title of the question"),
    "body": fields.String("Body/content of the question"),
    "votes": fields.Integer("Number of votes the question has received")
})

@qs_questions.route("")
class PostQuestion(Resource):
    @qs_questions.doc(security="apikey")
    @qs_questions.expect(mod_post_question)

    def post(self):
        args = parser.parse_args()
        createdOn = args["createdOn"]
        createdBy = args["createdBy"]
        meetup_id = args["meetup_id"]
        title = args["title"]
        body = args["body"]
        votes = args["votes"]


        question = question_models.Questions().post_question(createdOn, createdBy, meetup_id, title, body, votes)
        return {
            "status": 201,
            "message": "Question posted successfully.",
            "data": question
        }, 201