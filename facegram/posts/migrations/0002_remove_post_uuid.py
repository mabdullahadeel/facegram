# Generated by Django 3.1.13 on 2021-10-02 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='uuid',
        ),
    ]
