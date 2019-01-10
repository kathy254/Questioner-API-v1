import json

from .base_tests import BaseTest
from app.api.v1.models.question_models import Questions

post_question_url = "api/v1/questions"

class TestQuestions(BaseTest):

    def test_post_question(self):
        with self.client:
            question_payload = {
                "createdBy": 1,
                "meetup_id": 1,
                "title": "Git commands",
                "body": "What is the difference between git pull and git fetch?"
            }

            response = self.client.post(post_question_url, data=json.dumps(question_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "Question posted successfully.")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")