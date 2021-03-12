"""Error Response models"""


class ErrorResponseVo:
    """Error Response vo"""

    def __init__(self):
        self.error = None


class ErrorResponse:
    """Error Response"""

    def __init__(self):
        self.statusCode = None
        self.name = None
        self.message = None
