# Generated by Django 3.0.7 on 2021-03-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0032_invite_friends"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitefriends",
            name="invited",
            field=models.BooleanField(default=False),
        ),
    ]