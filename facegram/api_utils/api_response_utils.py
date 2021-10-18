from rest_framework import status
from rest_framework.response import Response



class APIResponse:
    @staticmethod
    def success(data, message="success", status_code=status.HTTP_200_OK) -> Response:
        return Response(
            {
                "data": data,
                "message": message,
                "error": False,
            }
            ,status=status_code
        )

    @staticmethod
    def error(data, message="Something went wrong", status_code=status.HTTP_400_BAD_REQUEST) -> Response:
        return Response(
            {
                "data": data,
                "message": message,
                "error": True,
            },
            status=status_code
        )