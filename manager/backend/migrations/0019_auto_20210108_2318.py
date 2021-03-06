# Generated by Django 3.0.7 on 2021-01-08 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0018_auto_20210107_1753"),
    ]

    operations = [
        migrations.AddField(
            model_name="friends",
            name="requested",
            field=models.ForeignKey(
                db_column="requested",
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requested",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="friends",
            name="requester",
            field=models.ForeignKey(
                db_column="requester",
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="requester",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="friends",
            name="status",
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("DFT", "Default"),
                    ("FRD_REQ", "Friend Request"),
                    ("FRD_ACPT", "Friend Acceptance"),
                    ("CMT", "Comment"),
                    ("LKT", "Link Taggs"),
                ],
                default="DFT",
                max_length=10,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="friends",
            unique_together={("requester", "requested")},
        ),
        migrations.RemoveField(
            model_name="friends",
            name="friend",
        ),
        migrations.RemoveField(
            model_name="friends",
            name="user",
        ),
    ]
