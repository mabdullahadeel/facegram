# Generated by Django 3.1.13 on 2021-10-02 22:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='postvotes',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
