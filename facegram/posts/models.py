from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

PRIVACY_CHOICES = (
    ('OM', "Only Me"),
    ('OF', "Only Friends"),
    ('EO', "Every One")
)

class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[
        FileExtensionValidator([
            'png', 'jpg', 'jpeg',
        ])
    ], blank=True, null=True)
    privacy = models.CharField(max_length=6, choices=PRIVACY_CHOICES, default='OM')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} - {self.author}"


    class Meta:
        ordering = ('-created_at',)


class PostVotes(models.Model):

    REACTION_CHOICES = (
        ('UV', 'upvote'),
        ('DV', 'downvote'),
    )

    post = models.ForeignKey(to=Post, related_name='post', on_delete=models.CASCADE)
    reaction = models.CharField(max_length=6, choices=REACTION_CHOICES)
    voters = models.ForeignKey(to=User, related_name='voters')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
