from flask import Flask, jsonify

from .api.v1 import app_v1
from instance.config import app_config


def create_app(config):
    """function creating the flask app"""
    app = Flask(__name__)
    app.register_blueprint(app_v1)
    app.config.from_object(app_config[config])

    return app
