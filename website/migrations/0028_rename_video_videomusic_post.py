# Generated by Django 4.1.2 on 2022-10-05 01:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0027_remove_comment_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="videomusic",
            old_name="video",
            new_name="post",
        ),
    ]
