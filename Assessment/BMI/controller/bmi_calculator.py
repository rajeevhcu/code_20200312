from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_api import status
from ..common import logger
from .. import db
from ..service.BMI_service import register_customer,get_overweight

log = logger.get_logger(__name__)
bp = Blueprint('user', __name__, url_prefix='/bmi')
api = Api(bp)


class CustomerRegistration(Resource):
    """
        Create new customer
    """

    def post(self):
        request_body = request.get_json()
        return register_customer(request_body)

    def get(self):
        return get_overweight()

api.add_resource(CustomerRegistration, '/customer-registration')
