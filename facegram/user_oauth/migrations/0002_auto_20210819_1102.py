# Generated by Django 3.1.13 on 2021-08-19 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oauthscopes',
            options={'verbose_name_plural': 'OAuth Scopes'},
        ),
    ]
