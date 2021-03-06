# Generated by Django 3.0.7 on 2022-02-10 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0106_merge_20220209_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggusermeta',
            name='dm_view_stage',
            field=models.IntegerField(choices=[(0, 'Not Viewed All Moments'), (1, 'Viewed All Moments'), (2, 'Revisiting Dm')], default=0),
        ),
        migrations.AddField(
            model_name='taggusermeta',
            name='timestamp_dm_view_stage',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 23, 46, 37, 118263, tzinfo=utc)),
        ),
    ]
