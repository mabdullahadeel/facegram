from uuid import UUID
from facegram.api_utils.api_response_utils import APIResponse
from rest_framework import status as http_status
from django.core.exceptions import ValidationError
from django.db.models import Q
from functools import wraps
from facegram.posts.models import PostComment, PostVotes, PostCommentVotes

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


def user_is_allowed_to_vote_on_post(func):
    """
        Check if the user is allowed to vote on a post
    """
    @wraps(func)
    def inner(*args, **kwargs):
        request = args[1]
        post_id = request.GET.get('post_id', None)
        if not post_id:
            return APIResponse.error(data=[], message='post_id is required')

        vote = PostVotes.objects.filter(Q(post__id=post_id) & Q(voter=request.user))
        if vote.exists() and vote.first().post.privacy == "OM":
            return APIResponse.error(data=[], message="action not allowed", status_code=http_status.HTTP_403_FORBIDDEN)
        
        kwargs['vote'] = vote.first()
        return func(*args, **kwargs)

    return inner


def is_user_allowed_to_vote_on_comment(func):
    """
        Check if the user is allowed to vote on a comment
    """
    @wraps(func)
    def inner(*args, **kwargs):
        request = args[1]
        comment_id: str = request.GET.get('comment_id', None)
        if not comment_id:
            return APIResponse.error(data=[], message='comment_id is required')

        comment_vote = PostCommentVotes.objects.filter(Q(id=comment_id) & Q(comment_voter=request.user))
        if comment_vote.exists() and comment_vote.first().post_comment.post.privacy == "OM":
            return APIResponse.error(data=[], message="action not allowed", status_code=http_status.HTTP_403_FORBIDDEN)
        
        kwargs['comment_vote'] = comment_vote.first()
        return func(*args, **kwargs)

    return inner
