from flask import Flask, request, jsonify, Blueprint, json, make_response
from flask_restplus import Resource, reqparse, Namespace, fields, Api

from ...v1.models import meetup_models


parser = reqparse.RequestParser()
parser.add_argument("createdOn", help="This field cannot be blank")
parser.add_argument("location", help="This field cannot be blank")
parser.add_argument("images", help="This field is optional")
parser.add_argument("topic", help="This field cannot be blank")
parser.add_argument("happeningOn", help="This field cannot be blank")
parser.add_argument("Tags", help="This field cannot be blank")


qs_meetups = Namespace("meetups", description="Meetups endpoints")
mod_create = qs_meetups.model("Create a new meetup", {
    "createdOn":fields.String("Date meetup was created"),
    "location":fields.String("Location of the meetup"),
    "images":fields.String("URL of the images"),
    "topic":fields.String("Topic to be discussed"),
    "happeningOn":fields.String("Date the meetup is happening"),
    "Tags":fields.String("Tags associated with this meetup")
})


@qs_meetups.route('')
class CreateMeetup(Resource):
    @qs_meetups.doc(security="apikey")
    @qs_meetups.expect(mod_create)
    def post(self):
        args = parser.parse_args()
        createdOn = args["createdOn"]
        location = args["location"]
        images = args["images"]
        topic = args["topic"]
        happeningOn = args["happeningOn"]
        Tags = args["Tags"]

        meetups = meetup_models.Meetups().create_meetup(createdOn, location, images, topic, happeningOn, Tags)
        return (
                {
                    "status": 201,
                    "message": "New meetup created successfully",
                    "data": meetups,
                },
                201,
            )

    
@qs_meetups.route('/upcoming')
class GetAllMeetups(Resource):
    @qs_meetups.doc(security="apikey")
    def get(self):
        all_meetups = meetup_models.meetup_list
        if len(all_meetups) == 0:
            return {
                "status": 404,
                "error": "No meetups found"
                }, 404

        else:
            return {
                    "status": 200,
                    "data": all_meetups
                }, 200
            