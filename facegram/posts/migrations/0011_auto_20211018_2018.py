# Generated by Django 3.1.13 on 2021-10-18 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_auto_20211018_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='likers',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='total_likes',
        ),
        migrations.CreateModel(
            name='PostCommentVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('reaction', models.CharField(choices=[('UV', 'upvote'), ('DV', 'downvote')], max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('comment_voter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comment_voter', to=settings.AUTH_USER_MODEL)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='posts.postcomment')),
            ],
            options={
                'verbose_name_plural': 'Post Comment Votes',
                'db_table': 'post_comment_votes',
            },
        ),
    ]
