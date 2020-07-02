def handle_error(response):
    codes = {-1: ZTFAPIError, 400: ParseError, 404: ObjectNotFoundError}
    error = response.json().get("errors", {})
    message = response.json().get("message")
    code = response.status_code
    data = error

    raise codes.get(code, ZTFAPIError)(
        message=message, code=code, data=data, response=response
    )


class ZTFAPIError(Exception):
    response = None
    data = {}
    message = "An error with the API occurred"
    code = -1

    def __init__(self, message=None, code=None, data={}, response=None):
        self.response = response
        if message:
            self.message = message
        if code:
            self.code = code
        if data:
            self.data = data

    def __str__(self):
        if self.code:
            ret = {"Error code": self.code, "Message": self.message, "Data": self.data}
            return str(ret)
        return self.message


class ParseError(ZTFAPIError):
    pass


class FormatValidationError(ParseError):
    pass


class ObjectNotFoundError(ZTFAPIError):
    ## TODO add logic for including oid in error message
    pass
