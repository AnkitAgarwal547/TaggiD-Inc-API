# Generated by Django 3.0.7 on 2022-01-31 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0089_auto_20220131_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationlinkwidget',
            name='font_color',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='genericlinkwidget',
            name='font_color',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='socialmediawidget',
            name='font_color',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='videolinkwidget',
            name='font_color',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
