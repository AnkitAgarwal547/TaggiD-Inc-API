# Generated by Django 3.0.7 on 2020-10-20 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_auto_20201019_1856"),
    ]

    operations = [
        migrations.CreateModel(
            name="MomentComments",
            fields=[
                (
                    "comment_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("comment", models.CharField(max_length=256)),
                ("date_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="follow",
            name="followed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="follow",
            name="follower",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follower",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddIndex(
            model_name="momentmetadata",
            index=models.Index(
                fields=["user_id"], name="backend_mom_user_id_d32c02_idx"
            ),
        ),
        migrations.AddField(
            model_name="momentcomments",
            name="commenter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="momentcomments",
            name="moment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.MomentMetadata"
            ),
        ),
        migrations.AddIndex(
            model_name="momentcomments",
            index=models.Index(
                fields=["comment_id"], name="backend_mom_comment_bae8c2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="momentcomments",
            index=models.Index(
                fields=["moment_id"], name="backend_mom_moment__6e3fb4_idx"
            ),
        ),
    ]