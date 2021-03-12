""" Error response preparation"""
from ..model.response import ErrorResponseVo
from ..model.response import ErrorResponse


def error_response_preparation(status_code, name, msg):
    """method to prepare error response"""
    error_response_vo = ErrorResponseVo()
    error_response = ErrorResponse()
    error_response.statusCode = status_code
    error_response.name = name
    error_response.message = str(msg)
    error_response_vo.error = error_response.__dict__
    return error_response_vo.__dict__
