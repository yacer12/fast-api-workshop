from fastapi.responses import JSONResponse
from fastapi import HTTPException



# Dictionary mapping status codes to messages
ERROR_MESSAGES = {
    400: "Bad request. The request is missing required fields.",
    401: "Unauthorized access. Please provide valid credentials.",
    403: "Forbidden. You do not have permission to access this resource.",
    404: "Resource not found. The requested item does not exist.",
    422: "Unprocessable entity. The request contains invalid data.",
    429: "Too many requests. Please try again later.",
}

class ErrorResponse():
    @classmethod
    def create_error_response(cls, status_code: int, custom_message:str = None) -> JSONResponse:
        """
        Creates a JSONResponse for the given status code using the predefined error messages.

        Args:
            status_code (int): The HTTP status code for the error.
            custom_message (str, optional): A custom message to include in the response. Defaults to None.

        Returns:
            JSONResponse: A JSON response with the error message and status code.
        """
        message = ERROR_MESSAGES.get(status_code, "An unknown error occurred.")
        if custom_message:
            message = f"{message} {custom_message}"
        return JSONResponse(
            content={"error": message, "status_code": status_code},
            status_code=status_code,
        )

