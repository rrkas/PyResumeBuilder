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
        verbose_name="Mobile",
    )

    address = models.TextField(verbose_name="Address")

    bio = models.TextField(verbose_name="Bio", max_length=150)


class TechnicalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    website = models.URLField(verbose_name="Website", null=True)
    github = models.URLField(verbose_name="Github", null=True)
    linkedin = models.URLField(verbose_name="LinkedIn", null=True)
    credly = models.URLField(verbose_name="Credly", null=True)

    @property
    def extra_links(self):
        class Temp:
            count = 1

            def __init__(self, name, url):
                self.name = name
                self.url = url
                self.index = Temp.count
                Temp.count += 1

        return [
            Temp(link.name, link.url)
            for link in TechnicalDetailsExtraURL.objects.filter(user=self.user)
        ]

    @property
    def links(self):
        class Temp:
            def __init__(self, name, url):
                self.name = name
                self.url = url

        t = [
            Temp("Website", self.website),
            Temp("Github", self.github),
            Temp("LinkedIn", self.linkedin),
            Temp("Credly", self.credly),
        ]
        return t


class TechnicalDetailsExtraURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)
    url = models.URLField()
