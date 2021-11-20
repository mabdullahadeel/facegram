import pytest

from facegram.posts.tests.factories import PostFactory
from facegram.posts.models import Post


@pytest.fixture
def post() -> Post:
    return PostFactory()