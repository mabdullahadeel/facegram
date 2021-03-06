# Generated by Django 3.1.13 on 2021-10-17 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20211002_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AlterModelOptions(
            name='postvotes',
            options={'verbose_name_plural': 'Post Votes'},
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='likers',
            field=models.ManyToManyField(blank=True, null=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
