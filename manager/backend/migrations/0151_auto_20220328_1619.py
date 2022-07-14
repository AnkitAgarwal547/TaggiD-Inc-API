# Generated by Django 3.0.7 on 2022-03-28 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0150_auto_20220323_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(default='', max_length=12, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('fullname', models.CharField(default='', max_length=110)),
                ('status', models.CharField(blank=True, choices=[('INVITE', 'Invite'), ('INVITED', 'Invited'), ('JOINED', 'Joined')], max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]