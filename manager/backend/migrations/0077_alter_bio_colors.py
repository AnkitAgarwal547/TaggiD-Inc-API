# Generated by Django 3.0.7 on 2021-11-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0076_add_username_to_smt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skin",
            name="bio_color_end",
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name="skin",
            name="bio_color_start",
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name="skin",
            name="bio_text_color",
            field=models.CharField(max_length=7, null=True),
        ),
    ]