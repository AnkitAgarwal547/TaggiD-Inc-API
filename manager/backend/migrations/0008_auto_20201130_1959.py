# Generated by Django 3.0.7 on 2020-11-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_blockeduser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sociallink",
            name="snapchat_url",
        ),
        migrations.RemoveField(
            model_name="sociallink",
            name="tiktok_url",
        ),
        migrations.AddField(
            model_name="sociallink",
            name="snapchat_username",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="sociallink",
            name="tiktok_username",
            field=models.CharField(default="", max_length=256),
        ),
    ]
