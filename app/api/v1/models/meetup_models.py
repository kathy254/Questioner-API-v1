from ...v1.utils.validations import Validations
import datetime

from ...v1.models import user_models


meetup_list = []

meetup_id = 1


class Meetups(Validations):
    """A class to represent the meetup model"""

    def create_meetup(self, createdOn, location, images, topic,
                      happeningOn, Tags):
        """method to add a meetup to the meetup list"""
        new_meetup = dict(
            meetup_id=len(meetup_list) + 1,
            createdOn=datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            location=location,
            images=images,
            topic=topic,
            happeningOn=happeningOn,
            Tags=Tags,
        )

        payload = location, topic, happeningOn, Tags
        strings = location, images, topic, Tags
        if self.is_empty(payload) is True:
            res = {"message": "Please fill out all fields"}, 406
        elif self.is_whitespace(payload) is True:
            res = {"message": "Data cannot contain whitespaces only"}, 406
        elif self.is_string(strings) is False:
            res = {"message": "Input must be of type string"}, 406
        elif self.is_valid_date(happeningOn) is False:
            res = {"message": "Date must be in the format DD-MM-YYYY"}
        else:
            res = meetup_list.append(new_meetup)
            return {
                "status": 201,
                "message": "New meetup created successfully",
                "data": new_meetup,
                }, 201
        return res

    def get_all_meetups(self):
        if len(meetup_list) == 0:
            res = False
        else:
            res = meetup_list
        return res

    @staticmethod
    def get_specific_meetup(meetup_id):
        meetup_item = [item for item in meetup_list if item["meetup_id"] == meetup_id]
        if meetup_item:
            return meetup_item
        return False