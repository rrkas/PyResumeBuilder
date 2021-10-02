# Generated by Django 3.2.7 on 2021-10-01 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("details", "0006_alter_generaldetails_bio"),
    ]

    operations = [
        migrations.CreateModel(
            name="TechnicalDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("website", models.URLField(null=True, verbose_name="Website")),
                ("github", models.URLField(null=True, verbose_name="Github")),
                ("linkedin", models.URLField(null=True, verbose_name="LinkedIn")),
                ("credly", models.URLField(null=True, verbose_name="Credly")),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TechnicalDetailsOtherURLs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField()),
                (
                    "technical_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="details.technicaldetails",
                    ),
                ),
            ],
        ),
    ]