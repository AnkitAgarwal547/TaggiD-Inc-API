# Generated by Django 3.0.7 on 2021-05-07 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("backend", "0043_increase_comment_length"),
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
                    ("SYSTEM_MSG", "System Msg"),
                ],
                default="DFT",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Reaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "reaction_type",
                    models.CharField(
                        choices=[("LIKE", "Like")], default="LIKE", max_length=10
                    ),
                ),
                ("reaction_object_id", models.UUIDField(null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommentsReactionList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "actor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.Reaction",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="reaction",
            index=models.Index(
                fields=["reaction_object_id", "reaction_type"],
                name="backend_rea_reactio_159046_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="reaction",
            unique_together={("reaction_object_id", "reaction_type")},
        ),
        migrations.AddIndex(
            model_name="commentsreactionlist",
            index=models.Index(
                fields=["reaction"], name="backend_com_reactio_ec1ac5_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="commentsreactionlist",
            unique_together={("reaction", "actor")},
        ),
    ]
