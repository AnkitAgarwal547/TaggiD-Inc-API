# Generated by Django 3.0.7 on 2022-01-27 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0085_gameprofile_rewards'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='MomentViews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('moment_visited', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Moment')),
            ],
        ),
        migrations.AddIndex(
            model_name='momentviews',
            index=models.Index(fields=['moment_visited', 'timestamp'], name='backend_mom_moment__cda92c_idx'),
        ),
    ]
