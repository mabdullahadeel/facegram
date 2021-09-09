from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[
        FileExtensionValidator([
            'png', 'jpg', 'jpeg',
        ])
    ], blank=True)
    upvotes = models.IntegerField(default=0)
    voters = models.ManyToManyField(to=User, related_name='voters')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} - {self.author}"


    class Meta:
        ordering = ('-created_at',)

