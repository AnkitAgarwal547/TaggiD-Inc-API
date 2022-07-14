# Generated by Django 3.0.7 on 2021-11-12 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0068_remove_moment_view_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='MomentEngagement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('view_duration', models.IntegerField(default=0)),
                ('clicked_on_profile', models.BooleanField(default=False)),
                ('clicked_on_comments', models.BooleanField(default=False)),
                ('clicked_on_share', models.BooleanField(default=False)),
                ('moment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Moment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='momentengagement',
            index=models.Index(fields=['user'], name='backend_mom_user_id_4d0971_idx'),
        ),
    ]