from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from resume_builder import settings as project_settings


class GeneralDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    image = models.ImageField(verbose_name="Image", upload_to="user_images", null=True)

    name = models.CharField(max_length=120, verbose_name="Name")
    dob = models.DateField(verbose_name="Date of Birth", null=True)
    email = models.EmailField(verbose_name="Email", unique=True, null=True)
    mobile = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                project_settings.PHONE_NUMBER_REGEX,
                "Invalid format! Format: +(1-3) (9-13)",
            )
        ],
        help_text="Format: +(1-3) (9-13)",
        unique=True,
        verbose_name="Mobile"
    )

    address = models.TextField(verbose_name="Address")

    bio = models.TextField(verbose_name="Bio", max_length=150)
