# Generated by Django 4.1.1 on 2022-09-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0007_rename_shows_show_video_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lucia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name="show",
            options={},
        ),
    ]
