from django.db import models


class OAuthScopes(models.Model):
    """
        Models stores Oauth scopes
    """
    PROVIDER_CHOICES = [
        ('FB', 'Facebook'),
        ('GH', 'GitHub'),
        ('TW', 'Twitter'),
        ('GL', 'Google'),
    ]
    scope = models.CharField(max_length=255, unique=True)
    provider = models.CharField(max_length=255, blank=False, null=False, choices=PROVIDER_CHOICES)
    ip = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.scope
