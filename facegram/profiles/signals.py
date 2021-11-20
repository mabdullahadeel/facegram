from django.db.models.signals import pre_save
from django.dispatch import receiver
from facegram.profiles.models import Profile
from .tasks import get_auth_provider_profile_pic


# @receiver(pre_save, sender=?)
# def user_logged_in_callback(sender, instance, **kwargs):
#     """
#         Create Profile instance when user signs up
#     """
#     if instance.provider == "github":
#         profile, created = Profile.objects.get_or_create(
#             user=instance.user,
#             location=instance.extra_data.get("location"),
#         )
#         if created:
#             profile.save()
#             get_auth_provider_profile_pic.delay(
#                 username=instance.user.username,
#                 pic_url=instance.extra_data.get("avatar_url"),
#                 provider="github")