# Generated by Django 3.1.13 on 2021-10-18 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20211018_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcommentvotes',
            name='uuid',
        ),
    ]
