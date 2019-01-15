from flask import Flask, request, jsonify, Blueprint, json, make_response
from flask_restplus import Resource, reqparse, Namespace, fields, Api

from ...v1.models import meetup_models
from ...v1.models import user_models


parser = reqparse.RequestParser()
parser.add_argument("createdOn", help="This field cannot be blank")
parser.add_argument("location", help="This field cannot be blank")
parser.add_argument("images", help="This field is optional")
parser.add_argument("topic", help="This field cannot be blank")
parser.add_argument("happeningOn", help="This field cannot be blank")
parser.add_argument("Tags", help="This field cannot be blank")


qs_meetups = Namespace("meetups", description="Meetups endpoints")
mod_create = qs_meetups.model("Create a new meetup", {
    "createdOn": fields.String("Date meetup was created"),
    "location": fields.String("Location of the meetup"),
    "images": fields.String("URL of the images"),
    "topic": fields.String("Topic to be discussed"),
    "happeningOn": fields.String("Date the meetup is happening"),
    "Tags": fields.String("Tags associated with this meetup")
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
        return {
            "status": 201,
            "message": "New meetup created successfully",
            "data": meetups,
            }, 201


@qs_meetups.route('/upcoming')
class GetAllMeetups(Resource):
    @qs_meetups.doc(security="apikey")
    def get(self):
        all_meetups = meetup_models.meetup_list
        if len(all_meetups) == 0:
            res = {
                "status": 404,
                "error": "No meetups found"
                }, 404
        else:
            res = {
                    "status": 200,
                    "data": all_meetups
                }, 200
        return res


@qs_meetups.route("/<int:meetup_id>")
class GetMeetupById(Resource):
    @qs_meetups.doc(security="apikey")
    def get(self, meetup_id):
        single_meetup = meetup_models.Meetups().get_specific_meetup(meetup_id)
        if single_meetup:
            res = {
                "status": 200,
                "data": single_meetup
            }, 200
        else:
            res = {
                "status": 404,
                "response": "Meetup record not found"
            }, 404
        return res

parser.add_argument("RSVP", help="This field cannot be blank")
mod_rsvp = qs_meetups.model("RSVP to a meetup", {
    "RSVP": fields.String("Must be a yes, no or maybe")
})


@qs_meetups.route("/<int:meetup_id>/rsvps")
class RsvpToMeetup(Resource):
    @qs_meetups.doc(security="apikey")
    @qs_meetups.expect(mod_rsvp)
    def post(self, meetup_id):
        args = parser.parse_args()
        RSVP = args["RSVP"]

        RSVP = RSVP.lower()
        meetup = meetup_models.Meetups().get_specific_meetup(meetup_id)

        if (RSVP != "yes" and RSVP != "no" and RSVP != "maybe"):
            res = {"error": "Status should be a yes, no or maybe"}, 400

        elif not meetup:
            res = {
                "status": 400,
                "message": "Meetup with id {} not found.".format(meetup_id)
            }, 400
        else:
            res = {
                "status": 201,
                "topic": meetup[0]["topic"],
                "RSVP": RSVP
            }, 201
        return res
