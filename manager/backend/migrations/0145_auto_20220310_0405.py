# Generated by Django 3.2.11 on 2022-03-10 04:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0144_merge_20220310_0405'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='gameprofile',
        #     name='eligible_for_unlock_tagg_bg',
        # ),
        migrations.AddField(
            model_name='taggbackgroundimageunlock',
            name='is_award_shown',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taggusermeta',
            name='timestamp_dm_view_stage',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 4, 5, 42, 102552, tzinfo=utc)),
        ),
    ]
