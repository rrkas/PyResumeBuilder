# Generated by Django 3.2.7 on 2021-10-02 13:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("details", "0008_auto_20211002_1619"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="TechnicalDetailsOtherURLs",
            new_name="TechnicalDetailsExtraURL",
        ),
    ]