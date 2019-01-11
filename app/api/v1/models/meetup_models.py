from ...v1.utils.validations import Validations
import datetime

from ...v1.models import user_models


meetup_list = []

meetup_id = 1



class Meetups(Validations):
    """A class to represent the meetup model"""

    def create_meetup(self, createdOn, location, images, topic, happeningOn, Tags):
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
            return {"error": "Please fill out all fields"}, 406
        elif self.is_whitespace(payload) is True:
            return {"error": "Data cannot contain white strings"}, 406
        elif self.is_string(strings) is False:
            return {"error": "Input must be of type string"}, 406
        elif self.is_valid_date(happeningOn) is False:
            return {"error": "Date must be in the format DD-MM-YYYY"}
        else:
            meetup_list.append(new_meetup)
            return new_meetup

    def get_all_meetups(self):
        if len(meetup_list) == 0:
            return False
        else:
            return meetup_list


    @staticmethod
    def get_specific_meetup(meetup_id):
        meetup_item = [item for item in meetup_list if item["meetup_id"] == meetup_id]
        if meetup_item:
            return meetup_item
        return {"message": "Meetup record not found"}

    




