from django.db import models
from django.contrib.auth import get_user_model
from facegram.extras import models as extras_models

User = get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True, null=True)
    followers=models.ManyToManyField(User, related_name='followers', blank=True)
    following=models.ManyToManyField(User, related_name='following', blank=True)
    follower_count=models.PositiveIntegerField(default=0)
    following_count=models.PositiveIntegerField(default=0)
    bio=models.TextField(max_length=500, blank=True, null=True)
    location=models.CharField(max_length=30, blank=True, null=True)
    interests=models.ManyToManyField(extras_models.Interests, blank=True)
    skills=models.ManyToManyField(extras_models.Skills, blank=True)
    up_votes=models.PositiveIntegerField(default=0)
    down_votes=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.user.username)

