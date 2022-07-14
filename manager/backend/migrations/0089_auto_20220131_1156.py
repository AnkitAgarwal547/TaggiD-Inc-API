# Generated by Django 3.0.7 on 2022-01-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0088_auto_20220127_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationlinkwidget',
            name='background_url',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AddField(
            model_name='socialmediawidget',
            name='background_url',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AddField(
            model_name='socialmediawidget',
            name='thumbnail_url',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AddField(
            model_name='videolinkwidget',
            name='background_url',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AlterField(
            model_name='applicationlinkwidget',
            name='link_type',
            field=models.CharField(choices=[('SPOTIFY', 'Spotify'), ('SOUNDCLOUD', 'Soundcloud'), ('APPLE_MUSIC', 'Apple Music'), ('APPLE_PODCAST', 'Apple Podcast'), ('POSHMARK', 'Poshmark'), ('DEPOP', 'Depop'), ('ETSY', 'Etsy'), ('SHOPIFY', 'Shopify'), ('AMAZON', 'Amazon'), ('AMAZON_AFFILIATE', 'Amazon Affiliate'), ('APP_STORE', 'App Store')], max_length=32),
        ),
        migrations.AlterField(
            model_name='taggusermeta',
            name='profile_tutorial_stage',
            field=models.IntegerField(choices=[(0, 'Show Tutorial Videos'), (1, 'Show Stewie Griffin'), (2, 'Show Post Moment 1'), (3, 'Track Login After Post Moment 1'), (4, 'Show Post Moment 2'), (5, 'Complete')], default=0),
        ),
    ]
