# Generated by Django 4.0.4 on 2022-05-06 13:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_rename_user_like_image_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]