# Generated by Django 3.2.7 on 2021-10-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("details", "0010_educationaldetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationaldetails",
            name="institute_address",
            field=models.CharField(
                max_length=150, null=True, verbose_name="Institute Address"
            ),
        ),
    ]
