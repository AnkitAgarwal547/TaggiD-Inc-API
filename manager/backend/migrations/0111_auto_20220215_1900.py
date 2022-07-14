# Generated by Django 3.0.7 on 2022-02-15 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0110_merge_20220215_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagguser',
            name='tiktok_handle',
            field=models.CharField(blank=True, max_length=8192),
        ),
        migrations.AlterField(
            model_name='taggusermeta',
            name='timestamp_dm_view_stage',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 18, 59, 58, 225428, tzinfo=utc)),
        ),
    ]
