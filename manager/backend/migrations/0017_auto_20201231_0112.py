# Generated by Django 3.0.7 on 2020-12-31 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0016_merge_20201230_2007"),
    ]

    operations = [
        migrations.AddField(
            model_name="sociallink",
            name="fb_token_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("DFT", "Default"),
                    ("FRD", "Friend"),
                    ("CMT", "Comment"),
                    ("LKT", "Link Taggs"),
                ],
                default="DFT",
                max_length=4,
            ),
        ),
    ]
