import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

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
    privacy = models.CharField(max_length=6, choices=PRIVACY_CHOICES, default='EO')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'posts'


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
    voter = models.ForeignKey(to=User, related_name='voter', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    reaction = models.CharField(max_length=6, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = 'post_votes'


    def __str__(self):
        return f"{self.post.id}-{self.voter.username}"



class PostComment(models.Model):
    post = models.ForeignKey(to=Post, related_name='related_post', on_delete=models.CASCADE)
    commenter = models.ForeignKey(to=User, related_name='commenter', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    body = models.TextField(max_length=755)
    total_likes = models.PositiveIntegerField(default=0)
    likers = models.ManyToManyField(to=User, related_name="likers")


    class Meta:
        db_table = 'post_comments'


    def __str__(self):
        return f"{self.post.id}-{self.total_likes}"
