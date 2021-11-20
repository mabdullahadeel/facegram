from typing import Dict, Optional


class TestAPIResponse:
    @staticmethod
    def success(data=[], message="success") -> Dict:
        return {
                "data": data,
                "message": message,
                "error": False,
            }

    @staticmethod
    def error(data=[], message="Something went wrong", skip_message: Optional[bool]=False) -> Dict:
        res = {
                "data": data,
                "message": message,
                "error": True,
            }
        if skip_message:
            del res["message"]
        return res

