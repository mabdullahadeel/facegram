from uuid import UUID
from facegram.api_utils.api_response_utils import APIResponse
from django.core.exceptions import ValidationError
from functools import wraps

def is_uuid_valid(func):
    """
        Checks if a given uuid is valid.

        :param uuid: uuid to check
    """
    @wraps(func) # allows to keep the original function name
    def inner(*args, **kwargs):
        uuid = kwargs.get('uuid')
        
        if uuid is None:
            return APIResponse.error(data=[], message="No data provided...")
        try:
            uuid_obj = UUID(uuid, version=4)
            if str(uuid_obj) != uuid:
                raise ValidationError("Invalid uuid")
            return func(*args, **kwargs)
        except ValueError:
            return APIResponse.error(data=[], message="Invalid uuid...")

    return inner