# Generated by Django 4.1.1 on 2022-10-02 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0015_post_image_alter_post_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="image",
            new_name="featured_image",
        ),
    ]
