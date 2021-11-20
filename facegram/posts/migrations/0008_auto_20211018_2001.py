# Generated by Django 3.1.13 on 2021-10-18 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20211018_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvotes',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
