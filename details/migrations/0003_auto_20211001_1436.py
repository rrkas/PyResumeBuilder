# Generated by Django 3.2.7 on 2021-10-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("details", "0002_alter_generaldetails_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="generaldetails",
            name="Date of Birth",
        ),
        migrations.RemoveField(
            model_name="generaldetails",
            name="Image",
        ),
        migrations.AddField(
            model_name="generaldetails",
            name="dob",
            field=models.DateField(null=True, verbose_name="Date of Birth"),
        ),
        migrations.AddField(
            model_name="generaldetails",
            name="image",
            field=models.ImageField(
                null=True, upload_to="user_images", verbose_name="Image"
            ),
        ),
    ]
