# Generated by Django 4.1.2 on 2023-02-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
