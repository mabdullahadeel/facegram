from uuid import UUID
from facegram.api_utils.api_response_utils import APIResponse
from rest_framework import status as http_status
from django.core.exceptions import ValidationError
from functools import wraps
from facegram.posts.models import Post

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
        
        post_id = request.GET.get('post_id', None)
        if not post_id:
            return APIResponse.error(data=[], message='post_id is required')

        post = Post.objects.filter(id=post_id)
        if not post.exists() or post.first().privacy == "OM":
            return APIResponse.error(data=[], message="user is not allowed to comment", status_code=http_status.HTTP_403_FORBIDDEN)
        
        kwargs['post'] = post.first()
        return func(*args, **kwargs)

    return inner
