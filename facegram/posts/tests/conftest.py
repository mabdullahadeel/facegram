import pytest

from facegram.posts.tests.factories import (
    PostFactory, PostCommentFactory, CommentVoteFactory 
)
from facegram.posts.models import Post


@pytest.fixture
def post() -> Post:
    return PostFactory()

@pytest.fixture
def public_post() -> Post:
    return PostFactory(privacy="EO")

@pytest.fixture
def comment():
    return PostCommentFactory()

@pytest.fixture
def comment_vote():
    return CommentVoteFactory()