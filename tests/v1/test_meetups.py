import json
import datetime

from .base_tests import BaseTest
from app.api.v1.models.meetup_models import Meetups

create_meetup_url = "api/v1/meetups"

class TestMeetups(BaseTest):

    def test_create_meetup(self):
        with self.client:
            meetup_payload = {"location": "roysambu", "images": "url", "topic": "topic", "happeningOn": "12-12-2019", "Tags": "python"}
            response = self.client.post(create_meetup_url, data=json.dumps(meetup_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))
            
            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "New meetup created successfully")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")
