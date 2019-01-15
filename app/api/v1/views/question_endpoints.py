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
        return question


@qs_questions.route("/<int:question_id>")
class SingleQuestion(Resource):
    @qs_questions.doc(security="apikey")
    def get(self, question_id):
        single_question = question_models.Questions().get_question_id(question_id)
        if single_question:
            return {
                "status": 200,
                "data": single_question
            }, 200
        return {
            "status": 404,
            "response": "Question not found"
        }, 404


@qs_questions.route("/<int:question_id>/upvote")
class UpvoteDownvote(Resource):
    @qs_questions.doc(security="apikey")
    def patch(self, question_id):
        one_question = question_models.Questions().get_question_id(question_id)
        if one_question:
            my_question = one_question[0]
            my_question["votes"] = my_question["votes"] + 1
            return {
                "status": 200,
                "data": my_question
            }, 200


@qs_questions.route("/<int:question_id>/downvote")
class DownvoteQuestion(Resource):
    @qs_questions.doc(security="apikey")
    def patch(self, question_id):
        one_question = question_models.Questions().get_question_id(question_id)
        if one_question:
            this_question = one_question[0]
            this_question["votes"] = this_question["votes"] - 1
            return {
                "status": 200,
                "data": this_question
            }, 200
