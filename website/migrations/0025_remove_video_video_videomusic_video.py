# Generated by Django 4.1.2 on 2022-10-05 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0024_video_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="video",
        ),
        migrations.AddField(
            model_name="videomusic",
            name="video",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="video",
                to="website.post",
            ),
        ),
    ]
