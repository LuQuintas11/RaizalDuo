# Generated by Django 4.1.2 on 2022-10-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_alter_comment_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]