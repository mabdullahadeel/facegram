from django.contrib.auth import get_user_model
from factory import Faker
import factory
from factory.django import DjangoModelFactory
from facegram.posts.models import Post
from facegram.users.tests.factories import UserFactory

User = get_user_model()
PRIVACY_OPTIONS = ("OM", "OF", "EO")

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post


    author = factory.SubFactory(UserFactory)
    title = Faker('sentence')
    body = Faker('text')
    image = factory.django.ImageField(color='blue', format='JPEG')
    privacy = factory.Iterator(PRIVACY_OPTIONS)


