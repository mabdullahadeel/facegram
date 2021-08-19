from django.db.models.signals import pre_save
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
import json
from facegram.profiles.models import Profile


@receiver(pre_save, sender=SocialAccount)
def user_logged_in_callback(sender, instance, **kwargs):
    """
        Create Profile instance when user signs up
    """
    if instance.provider == "github":
        profile = Profile.objects.create(
            user=instance.user,
            profile_pic=instance.extra_data.get("avatar_url"),
            location=instance.extra_data.get("location"),
        )
        profile.save()