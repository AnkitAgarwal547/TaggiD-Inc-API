# Generated by Django 3.0.7 on 2022-02-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0103_auto_20220209_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagguser',
            name='reward',
            field=models.CharField(blank=True, choices=[('BLOCKED', 'Blocked'), ('UNBLOCKED', 'Unblocked')], max_length=50, null=True),
        ),
    ]
