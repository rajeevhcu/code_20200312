from flask import jsonify
from flask_api import status

from .. import error_response_preparation, db
from ..common import logger, constants
from ..model.bmi import BMI

log = logger.get_logger(__name__)


def get_overweight():
    """
    :return: Total number of overweight customer
    """
    try:
        log.info("Entry into get_overweight")
        bmi_obj = BMI.query.filter(BMI.bmi_category == constants.CATEGORY_AND_RISK[3]['category']).count()
        return {"Total overweight": bmi_obj}
    except Exception as err:
        log.error("Error in get_overweight: " + str(err))
        response = error_response_preparation(
            status.HTTP_500_INTERNAL_SERVER_ERROR, constants.RESPONSE_ERROR, constants.ERROR)
        return response, status.HTTP_500_INTERNAL_SERVER_ERROR


def register_customer(req_body):
    """
    Method to calculate bmi, category and rink and save the customer record as new customer
    :param req_body: {"gender":"Male","height_cm":150,"weight_kg":70}
    :return: BMI object
    """
    try:
        log.info('Entry into register_customer')
        gender = req_body.get('gender', None)
        height_cm = req_body.get('height_cm', None)
        weight_kg = req_body.get('weight_kg', None)
        error, code = param_validation(gender, height_cm, weight_kg)
        if error is not None:
            log.error(
                "Validation error in register_customer : " + str(error))
            response = error_response_preparation(code, constants.RESPONSE_ERROR, error)
            return response, code
        bmi = calculate_bmi(height_cm, weight_kg)
        category = get_cate_risk(bmi)
        bmi_obj = BMI(gender=gender,
                      height_cm=height_cm,
                      weight_kg=weight_kg,
                      bmi=bmi,
                      bmi_category=category['category'],
                      health_risk=category['risk'])
        db.session.add(bmi_obj)
        db.session.commit()
        response = prepare_json(bmi_obj)
        response["msg"] = "Customer registered successfully."
        return jsonify(response)
    except Exception as err:
        db.session.rollback()
        log.error("Error in register customer post method: " + str(err))
        response = error_response_preparation(
            status.HTTP_500_INTERNAL_SERVER_ERROR, constants.RESPONSE_ERROR, constants.ERROR)
        return response, status.HTTP_500_INTERNAL_SERVER_ERROR


def calculate_bmi(height, weight):
    """
    Method to calculate BMI
    :param height: cm
    :param weight: kg
    :return:
    """
    try:
        return round((weight * 100) / height, 2)
    except Exception as err:
        raise err


def get_cate_risk(bmi):
    """
    Method to find category and risk based on BMI
    :param bmi: BMI value
    :return: Dict of category and health risk
    """
    try:
        if bmi <= 18.4:
            return constants.CATEGORY_AND_RISK[1]
        elif 18.5 >= bmi <= 24.9:
            return constants.CATEGORY_AND_RISK[2]
        elif 25 >= bmi <= 29.9:
            return constants.CATEGORY_AND_RISK[3]
        elif 30 >= bmi <= 34.9:
            return constants.CATEGORY_AND_RISK[4]
        elif 35 >= bmi <= 39.9:
            return constants.CATEGORY_AND_RISK[5]
        else:
            return constants.CATEGORY_AND_RISK[6]
    except Exception as err:
        raise err


def param_validation(gender, height_cm, weight_kg):
    """
    Method to validate parameters
    """
    try:
        msg = None
        code = status.HTTP_400_BAD_REQUEST
        if gender in ['', None]:
            msg = "Gender is required and can't be blank"
        elif height_cm in ['', None]:
            msg = "Height is required and can't be blank"
        elif weight_kg in ['', None]:
            msg = "Weight is required and can't be blank"
        return msg, code
    except Exception as err:
        raise Exception(err)


def prepare_json(row):
    """method to get json data from table row"""
    response = {}
    for column in row.__table__.columns:
        response[column.name] = getattr(row, column.name)
    return response
