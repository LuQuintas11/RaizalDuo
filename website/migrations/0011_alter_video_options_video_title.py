# Generated by Django 4.1.1 on 2022-10-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0010_delete_lucia"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="video",
            options={"ordering": ["-status"]},
        ),
        migrations.AddField(
            model_name="video",
            name="title",
            field=models.CharField(default=0, max_length=200),
        ),
    ]
