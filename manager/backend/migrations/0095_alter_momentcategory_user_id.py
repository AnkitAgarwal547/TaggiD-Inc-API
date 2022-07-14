# Generated by Django 3.2.11 on 2022-02-03 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0094_momentcategorylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='momentcategory',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]