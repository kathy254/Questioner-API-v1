import json

from .base_tests import BaseTest
from app.api.v1.models.question_models import Questions

post_question_url = "api/v1/questions"
upvote_url = "/api/v1/questions/1/upvote"

class TestQuestions(BaseTest):

    def test_post_question(self):
        with self.client:
            question_payload = {
                "createdBy": 1,
                "meetup_id": 1,
                "title": "Git commands",
                "body": "What is the difference between git pull and git fetch?",
                "votes": 0
            }

            response = self.client.post(post_question_url, data=json.dumps(question_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "Question posted successfully.")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")

    def test_upvote_question(self):
        with self.client:
            question_one = {
                "createdBy": 1,
                "meetup_id": 1,
                "title": "Artificial intelligence",
                "body": "What is the difference between statistical AI and classical AI?",
                "votes": 0
            }

            self.client.post(post_question_url, data=json.dumps(question_one), content_type = "application/json")

            response = self.client.patch(upvote_url, content_type = ("application/json"))
            self.assertEqual(response.status_code, 200)


