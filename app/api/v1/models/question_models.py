import datetime
from ...v1.utils.validations import Validations

question_list = []

question_id = 1

class Questions(Validations):

    def post_question(self, createdOn, createdBy, meetup_id, title, body, votes):
        new_question = dict(
            question_id = len(question_list) + 1,
            createdOn = datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            createdBy = createdBy,
            meetup_id = meetup_id,
            title = title,
            body = body,
            votes = 0
        )

        question_list.append(new_question)
        return new_question

    @staticmethod
    def get_question_id(question_id):
        question_item = [question for question in question_list if question["question_id"] == question_id]
        if question_item:
            return question_item
        else:
            return "Question not found"