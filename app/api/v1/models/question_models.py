import datetime
from ...v1.utils.validations import Validations

question_list = []

question_id = 1


class Questions(Validations):

    def post_question(self, createdOn, createdBy, meetup_id, title, body, votes):
        new_question = dict(
            question_id=len(question_list) + 1,
            createdOn=datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            createdBy=createdBy,
            meetup_id=meetup_id,
            title=title,
            body=body,
            votes=0
        )

        payload = createdBy, meetup_id, title, body

        if self.is_empty(payload) is True:
            res = {"message": "Please fill out all the fields"}, 406
        elif self.is_whitespace(payload) is True:
            res = {"message": "Data cannot contain whitespaces only"}, 406
        else:
            res = question_list.append(new_question)
            return {
                "status": 201,
                "message": "Question posted successfully.",
                "data": new_question
            }, 201

        return res

    @staticmethod
    def get_question_id(question_id):
        question_item = [question for question in question_list if question["question_id"] == question_id]
        if question_item:
            res = question_item
        else:
            res = False
        return res
