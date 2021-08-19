from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='skill_icons', null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)

    def __str__(self) -> str:
        return self.name


class Interests(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

