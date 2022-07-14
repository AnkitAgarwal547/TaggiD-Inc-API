# Generated by Django 3.0.7 on 2021-03-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0030_auto_20210226_2306"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscoverCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("category", models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name="discovercategory",
            index=models.Index(fields=["id"], name="backend_dis_id_317d57_idx"),
        ),
    ]
