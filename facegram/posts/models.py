import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model

User = get_user_model()

PRIVACY_CHOICES = (
    ('OM', "Only Me"),
    ('OF', "Only Followers"),
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
    uuid = models.CharField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'posts'


    def __str__(self):
        return f"{self.title} - {self.author}"


class PostVotes(models.Model):

    REACTION_CHOICES = (
        ('UV', 'upvote'),
        ('DV', 'downvote'),
    )

    post = models.ForeignKey(to=Post, related_name='post', on_delete=models.CASCADE)
    voter = models.OneToOneField(to=User, related_name='voter', on_delete=models.CASCADE)
    uuid = models.CharField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
    reaction = models.CharField(max_length=6, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = 'post_votes'
        verbose_name_plural = "Post Votes"


    def __str__(self):
        return f"{self.post.id}-{self.voter.username}"



class PostComment(models.Model):
    post = models.ForeignKey(to=Post, related_name='related_post', on_delete=models.CASCADE)
    commenter = models.ForeignKey(to=User, related_name='commenter', on_delete=models.CASCADE)
    uuid = models.CharField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
    body = models.TextField(max_length=755)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post_comments'
        verbose_name_plural = "Post Comments"


    def __str__(self):
        return f"{self.post.id}-{self.commenter}"


class PostCommentVotes(models.Model):
    
        REACTION_CHOICES = (
            ('UV', 'upvote'),
            ('DV', 'downvote'),
        )
    
        post_comment = models.ForeignKey(to=PostComment, related_name='post_comment', on_delete=models.CASCADE)
        comment_voter = models.OneToOneField(to=User, related_name='comment_voter', on_delete=models.CASCADE)
        uuid = models.CharField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
        reaction = models.CharField(max_length=6, choices=REACTION_CHOICES)
        created_at = models.DateTimeField(auto_now_add=True)
        last_modified = models.DateTimeField(auto_now=True)
    
        
        class Meta:
            db_table = 'post_comment_votes'
            verbose_name_plural = "Post Comment Votes"
    
    
        def __str__(self):
            return f"{self.post_comment.id}-{self.comment_voter.username}"
