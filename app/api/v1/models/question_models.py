import datetime

question_list = []

question_id = 1

class Questions:

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



