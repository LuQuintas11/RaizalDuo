# Generated by Django 3.2.15 on 2022-09-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_alter_post_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shows",
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
                ("show", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("excerpt", models.TextField(blank=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="website"),
        ),
    ]
