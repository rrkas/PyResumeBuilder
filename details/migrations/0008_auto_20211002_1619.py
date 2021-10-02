# Generated by Django 3.2.7 on 2021-10-02 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("details", "0007_technicaldetails_technicaldetailsotherurls"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="technicaldetailsotherurls",
            name="technical_detail",
        ),
        migrations.AddField(
            model_name="technicaldetailsotherurls",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
