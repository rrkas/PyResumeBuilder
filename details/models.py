from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

from resume_builder import settings as project_settings


# 1 for each user
class GeneralDetail(models.Model):
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
        verbose_name="Mobile",
    )

    address = models.TextField(verbose_name="Address")

    bio = models.TextField(verbose_name="Bio", max_length=150)


# 1 for each user
class TechnicalDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    website = models.URLField(verbose_name="Website", null=True)
    github = models.URLField(verbose_name="Github", null=True)
    linkedin = models.URLField(verbose_name="LinkedIn", null=True)
    credly = models.URLField(verbose_name="Credly", null=True)

    @property
    def extra_links(self):
        links = TechnicalDetailsExtraURL.objects.filter(user=self.user)
        for i, link in enumerate(links):
            link.__setattr__("index", i + 1)
        return links

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


# many for each user
class TechnicalDetailsExtraURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)
    url = models.URLField()


# many for each user
class EducationalDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    educational_level = models.CharField(
        max_length=120,
        verbose_name="Education Level",
    )

    # institute details
    institute_name = models.CharField(max_length=150, verbose_name="Institute Name")
    institute_address = models.CharField(
        max_length=150, verbose_name="Institute Address", null=True
    )

    # passing details
    year_of_admission = models.IntegerField(verbose_name="Year of admission", null=True)
    year_of_passing = models.IntegerField(verbose_name="Year of passing")
    percentage = models.DecimalField(
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        verbose_name="Percentage",
        help_text="0.00 - 100.00",
        max_digits=5,
        decimal_places=2,
    )
    cgpa = models.DecimalField(
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name="Cumulative Grade Points Average (CGPA)",
        help_text="0.00 - 10.00",
        max_digits=4,
        decimal_places=2,
    )

    # academic
    major_subject = models.CharField(max_length=120, null=True)

    class Meta:
        unique_together = (("user", "educational_level"),)

    @property
    def cgpa_percentage(self):
        if self.cgpa:
            return round(float(self.cgpa) * 9.5, 2)

    def clean(self):
        super(EducationalDetail, self).clean()
        if self.percentage is None and self.cgpa is None:
            raise ValidationError("Percentage and CGPA both null!")
        elif self.percentage is not None and self.cgpa is not None:
            raise ValidationError("Percentage and CGPA both not null!")

    def __repr__(self):
        return f"{self.user.email} - {self.educational_level}"

    def __str__(self):
        # shows in admin.site
        return f"{self.pk} : {self.user.email} - {self.educational_level}"


# many for each user
class ExperienceItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    experience_type = models.CharField(
        verbose_name="Type",
        max_length=20,
        choices=(
            ("job", "Job"),
            ("internship", "Internship"),
        ),
        default="job",
    )

    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date", null=True)

    institute_name = models.CharField(max_length=150, verbose_name="Institute Name")
    institute_address = models.CharField(
        max_length=150, verbose_name="Institute Address", null=True
    )

    reference_person_name = models.CharField(
        verbose_name="Reference Person Name",
        max_length=100,
        null=True,
    )
    reference_person_mobile = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                project_settings.PHONE_NUMBER_REGEX,
                "Invalid format! Format: +(1-3) (9-13)",
            )
        ],
        help_text="Format: +(1-3) (9-13)",
        verbose_name="Reference Person Mobile",
    )

    skills = models.TextField(verbose_name="Skills", null=True)

    document_url = models.URLField(
        verbose_name="Document URL",
        null=True,
    )

    def clean(self):
        super().clean()
        if (
            len(self.reference_person_mobile or "") != 0
            and len(self.reference_person_name or "") == 0
        ):
            raise ValidationError("Reference person mobile without name!")

    def skill_list(self):
        skills = list(map(lambda x: x.strip(), str(self.skills).split(";")))
        skills = [skills[::2], skills[1::2]]
        return skills
