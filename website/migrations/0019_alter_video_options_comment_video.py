# Generated by Django 4.1.1 on 2022-10-02 23:08

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0018_alter_video_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="video",
            options={},
        ),
        migrations.AddField(
            model_name="comment",
            name="video",
            field=embed_video.fields.EmbedVideoField(default=False),
        ),
    ]
