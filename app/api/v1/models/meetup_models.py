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
        meetup_item = [meetup for meetup in meetup_list if meetup["meetup_id"] == meetup_id]
        if meetup_item:
            res = meetup_item
        else:
            res = False
        return res

    @staticmethod
    def get_meetup_by_topic(topic):
        current_meetup = [meetup for meetup in meetup_list if meetup["topic"] == topic]
        if current_meetup:
            res = current_meetup
        else:
            res = False
        return res

    @staticmethod
    def get_meetup_by_location(location):
        current_location = [location for location in meetup_list if location["location"] == location]
        if current_location:
            res = current_location
        else:
            res = False
        return res

    @staticmethod
    def get_meetup_by_date(happeningOn):
        current_date = [date for date in meetup_list if date["happeningOn"] == happeningOn]
        if current_date:
            res = current_date
        else:
            res = False
        return res
