from flask import Blueprint
from flask_restplus import Api

from ..v1.views.meetup_endpoints import qs_meetups
from ..v1.views.user_endpoints import qs_users

authorizations = {
    "apikey": {
        "type": "apikey",
        "in": "header",
        "name": "Authorization"
    }
}

app_v1 = Blueprint("app_v1", __name__, url_prefix="/api/v1")
api_v1 = Api(app_v1, title="Questioner", version="1.0", description="Questioner API version 1", authorizations="authorizations")


api_v1.add_namespace(qs_meetups)
api_v1.add_namespace(qs_users)

