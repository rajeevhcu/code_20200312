from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_api import status
from flask_cors import CORS

from .common import logger, constants
from .common.error_response import error_response_preparation
from .config import mysql_config

log = logger.get_logger(__name__)

global db


def page_not_found(e):
    # note that we set the 404 status explicitly
    response = error_response_preparation(
        404,
        constants.CLIENT_ERROR,
        "Page Not Found"
    )
    return response, status.HTTP_404_NOT_FOUND


def internal_server_error(e):
    # note that we set the 500 status explicitly
    response = error_response_preparation(
        500,
        constants.RESPONSE_ERROR,
        "Internal Server Error"
    )
    return response, status.HTTP_500_INTERNAL_SERVER_ERROR


def create_app():
    """ to create and configure the flask application."""
    try:
        app = Flask(__name__, instance_relative_config=True)
        CORS(app)
        app.url_map.strict_slashes = False
        app.config.from_object(mysql_config.Config)
        global db
        db = SQLAlchemy(app)
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, internal_server_error)

        @app.route('/')
        def home():
            return """Welcome to BMI calculator"""

        from .controller.bmi_calculator import bp
        app.register_blueprint(bp)
        return app
    except Exception as err:
        log.info(err)
        raise err
