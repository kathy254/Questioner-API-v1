import json

from .base_tests import BaseTest
from app.api.v1.models.question_models import Questions

post_question_url = "/api/v1/questions"
get_single_url = "/api/v1/questions/1"
get_wrong_url = "/api/v1/questions/5"
upvote_url = "/api/v1/questions/1/upvote"
downvote_url = "/api/v1/questions/1/downvote"


class TestQuestions(BaseTest):
    def setUp(self):
        super().setUp()
        self.question_payload = {"createdBy": 1, "meetup_id": 1, "title": "Git commands", 
                                 "body": "What is the difference between git pull and git fetch?",
                                 "votes": 0
                                 }

        self.question_one = {"createdBy": 1, "meetup_id": 1, "title": "Artificial intelligence",
                             "body": "What is the difference between statistical AI and classical AI?",
                             "votes": 0
                             }

        self.whitespace_payload = {"createdBy": 1, "meetup_id": 1, "title": "  ", 
                                   "body": "What is the difference between git pull and git fetch?",
                                   "votes": 0
                                   }

    def test_post_question(self):
        with self.client:
            response = self.client.post(post_question_url, data=json.dumps(self.question_payload), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["status"], 201)
            self.assertEqual(result["message"], "Question posted successfully.")
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.content_type == "application/json")

    def test_empty_data(self):
        with self.client:
            response = self.client.post(post_question_url, data=json.dumps(""), content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["message"], "Please fill out all the fields")
            self.assertEqual(response.status_code, 406)
            self.assertTrue(response.content_type == "application/json")

    def test_whitespace_data(self):
        with self.client:
            response = self.client.post(post_question_url, data=json.dumps(self.whitespace_payload),
                        content_type="application/json")
            result = json.loads(response.data.decode("UTF-8"))

            self.assertEqual(result["message"], "Data cannot contain whitespaces only")
            self.assertEqual(response.status_code, 406)
            self.assertTrue(response.content_type == "application/json")

    def test_get_single_questions(self):
        self.client.post(post_question_url, data=json.dumps(self.question_payload), content_type="application/json")

        result = self.client.get(get_single_url)
        self.assertEqual(result.status_code, 200)

    def test_question_not_found(self):
        result = self.client.get(get_wrong_url)
        response = json.loads(result.data.decode("UTF-8"))

        self.assertEqual(response["status"], 404)
        self.assertEqual(response["response"], "Question not found")
        self.assertEqual(result.status_code, 404)


    def test_upvote_question(self):
        with self.client:
            self.client.post(post_question_url, data=json.dumps(self.question_one), content_type = "application/json")

            response = self.client.patch(upvote_url, content_type = "application/json")
            self.assertEqual(response.status_code, 200)

    def test_downvote_question(self):
        with self.client:
            self.client.post(post_question_url, data=json.dumps(self.question_one), content_type = "application/json")

            response2 = self.client.patch(downvote_url, content_type="application/json")
            self.assertEqual(response2.status_code, 200)

