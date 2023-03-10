# Generated by Django 4.1.6 on 2023-02-06 12:11

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/avatars/contacts-location.svg', null=True, upload_to=app_users.models.user_directory_path, verbose_name='Avatar'),
        ),
    ]
