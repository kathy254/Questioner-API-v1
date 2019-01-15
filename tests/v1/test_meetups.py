import json
import datetime

from .base_tests import BaseTest
from app.api.v1.models.meetup_models import Meetups

create_meetup_url = "/api/v1/meetups"
get_all_url = "/api/v1/meetups/upcoming"
get_one_url = "/api/v1/meetups/1"
rsvp_url = "/api/v1/meetups/1/rsvps"
wrong_rsvp_url = "/api/v1/meetups/3/rsvps"


class TestMeetups(BaseTest):

    def setUp(self):
        super().setUp()
        self.meetup_payload = {"location": "roysambu", "images": "url", "topic": "topic", "happeningOn": "12-12-2019", "Tags": "python"}
        self.whitespace_payload = {"location": " ", "images": "url", "topic": "topic", "happeningOn": "12-12-2019", "Tags": "python"}
        self.rsvp_payload = {"RSVP": "yes"}

    def tearDown(self):
        super().tearDown()
        self.meetup_payload = None
        self.whitespace_payload = None
        self.rsvp_payload = None

    def test_create_meetup(self):
        with self.client:
            response = self.client.post(create_meetup_url, data=json.dumps(self.meetup_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "New meetup created successfully")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")

    def test_empty_fields(self):
        with self.client:
            response1 = self.client.post(create_meetup_url, data=json.dumps(""), content_type="application/json")
            result1 = json.loads(response1.data.decode("UTF-8"))

            self.assertEqual(result1["message"], "Please fill out all fields")
            self.assertEqual(response1.status_code, 406)
            self.assertTrue(response1.content_type == "application/json")

    def test_white_space(self):
        """ test if data set has whitespace only"""
        with self.client:
            response2 = self.client.post(create_meetup_url, data=json.dumps(self.whitespace_payload), content_type="application/json")
            result2 = json.loads(response2.data.decode("UTF-8"))

            self.assertEqual(result2["message"], "Data cannot contain whitespaces only")
            self.assertEqual(response2.status_code, 406)
            self.assertTrue(response2.content_type == "application/json")

    def test_get_all_meetups(self):
        self.client.post(create_meetup_url, data=json.dumps(self.meetup_payload), content_type="application/json")

        result1 = self.client.get(get_all_url)
        self.assertEqual(result1.status_code, 200)

    def test_no_meetups_found(self):

        result3 = self.client.get(get_all_url)
        self.assertEqual(result3.status_code, 404)

    def test_get_specific_meetup(self):
        self.client.post(create_meetup_url, data=json.dumps(self.meetup_payload), content_type="application/json")

        result2 = self.client.get(get_one_url)
        self.assertEqual(result2.status_code, 200)

    def test_rsvp_meetup(self):

        self.client.post(create_meetup_url, data=json.dumps(self.meetup_payload), content_type="application/json")

        response8 = self.client.post(rsvp_url, data=json.dumps(self.rsvp_payload), content_type="application/json")
        result8 = json.loads(response8.data.decode("UTF-8"))

        self.assertEqual(result8["status"], 201)
        self.assertEqual(response8.status_code, 201)
        self.assertTrue(response8.content_type == "application/json")

    def test_rsvp_meetup_not_found(self):
        response9 = self.client.post(wrong_rsvp_url, data=json.dumps(self.rsvp_payload), content_type="application/json")
        result9 = json.loads(response9.data.decode("UTF-8"))

        self.assertEqual(result9["status"], 400)
        self.assertEqual(result9["message"], "Meetup with id 3 not found.")
        self.assertEqual(response9.status_code, 400)

    def test_wrong_rsvp_payload(self):
        self.client.post(create_meetup_url, data=json.dumps(self.meetup_payload), content_type="application/json")

        wrong_rsvp = {"RSVP": "Why"}

        response4 = self.client.post(rsvp_url, data=json.dumps(wrong_rsvp), content_type="application/json")
        result4 = json.loads(response4.data.decode("UTF-8"))

        self.assertEqual(result4["error"], "Status should be a yes, no or maybe")
        self.assertEqual(response4.status_code, 400)
