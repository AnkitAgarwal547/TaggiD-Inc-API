# Generated by Django 3.0.7 on 2021-01-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0017_auto_20201231_0112"),
    ]

    operations = [
        migrations.AddField(
            model_name="tagguser",
            name="profile_completion_stage",
            field=models.IntegerField(
                choices=[
                    (1, "Stage 1"),
                    (2, "Stage 2"),
                    (3, "Stage 3"),
                    (4, "Complete"),
                ],
                default=1,
            ),
        ),
    ]