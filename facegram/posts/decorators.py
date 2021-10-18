from uuid import UUID
from facegram.api_utils.api_response_utils import APIResponse
from rest_framework import status as http_status
from django.core.exceptions import RequestDataTooBig, ValidationError
from functools import wraps
from facegram.posts.models import PostComment

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



def user_is_allowed_to_comment(func):
    """
        General Validations for post commenting
    """
    @wraps(func)
    def inner(*args, **kwargs):

        request = args[1]
        
        comment_id: str = request.GET.get('comment_id', None)
        if not comment_id:
            return APIResponse.error(data=[], message='comment_id is required')

        comment = PostComment.objects.filter(id=comment_id)
        if not comment.exists() or comment.first().post.privacy == "OM":
            return APIResponse.error(data=[], message="action not allowed", status_code=http_status.HTTP_403_FORBIDDEN)
        
        kwargs['comment'] = comment.first()
        return func(*args, **kwargs)

    return inner
