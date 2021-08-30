from django.db.models.signals import pre_save
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from facegram.profiles.models import Profile
from .tasks import get_auth_provider_profile_pic


@receiver(pre_save, sender=SocialAccount)
def user_logged_in_callback(sender, instance, **kwargs):
    """
        Create Profile instance when user signs up
    """
    if instance.provider == "github":
        profile, created = Profile.objects.get_or_create(
            user=instance.user,
            location=instance.extra_data.get("location"),
        )
        profile.save()
        if created:
            print("requesting the image from github")
            profile.save()
            get_auth_provider_profile_pic(
                username=instance.user.username,
                pic_url=instance.extra_data.get("avatar_url"),
                provider="github")