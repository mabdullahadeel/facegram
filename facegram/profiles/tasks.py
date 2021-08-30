import requests
import tempfile
from django.core import files
from config import celery_app
from .models import Profile
import logging

logger = logging.getLogger(__name__)

@celery_app.task()
def get_auth_provider_profile_pic(username, pic_url, provider):
    """
        Download the profile picture from the auth provider
        and save it to the User Profile model.
    """

    response = requests.get(pic_url, stream=True)
    if response.status_code != 200:
        logger.error("Error downloading profile picture for user: %s, status_code=%s" % username, response.status_code)
        return
        
    extension = ".png"
    file_name = f"{username}_{provider}_profile" + extension
    temp_img = tempfile.NamedTemporaryFile(suffix=".jpg", prefix=file_name, delete=False)

    for block in response.iter_content(1024 * 8):
        if not block:
            break
        temp_img.write(block)

    user_profile = Profile.objects.get(user__username=username)
    user_profile.profile_pic.save(file_name, files.File(temp_img))
    

