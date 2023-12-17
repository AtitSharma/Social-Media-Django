# Generated by Django 5.0 on 2023-12-16 10:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='liked_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='post.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='post.post'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_image_post', to='post.post'),
        ),
        migrations.AddField(
            model_name='sharedpost',
            name='post',
            field=models.ManyToManyField(related_name='post_sharer_post', to='post.post'),
        ),
        migrations.AddField(
            model_name='sharedpost',
            name='user',
            field=models.ManyToManyField(related_name='user_sharer_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('post', 'liked_user'), name='unique_like'),
        ),
    ]