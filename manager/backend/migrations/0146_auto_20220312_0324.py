# Generated by Django 3.2.11 on 2022-03-12 03:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0145_auto_20220310_0405"),
    ]

    operations = [
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
                    ("MOM_3+", "Moment 3P"),
                    ("MOM_FRIEND", "Moment Friend"),
                    ("INVT_ONBRD", "Invitee Onboarded"),
                    ("MOM_TAG", "Moment Tag"),
                    ("SYSTEM_MSG", "System Msg"),
                    ("P_VIEW", "Profile View"),
                    ("M_VIEW", "Moment View"),
                    ("CLICK_TAG", "Click Tag"),
                ],
                default="DFT",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="ProfileViewNotificationTrigger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
