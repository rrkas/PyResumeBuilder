import django.forms as forms

from details.models import (
    GeneralDetail,
    TechnicalDetail,
    TechnicalDetailsExtraURL,
    EducationalDetail,
)


class GeneralDetailsEditForm(forms.ModelForm):
    class Meta:
        model = GeneralDetail
        exclude = ["user"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "House/ Plot/ Landmark, Street\n"
                    "City, District\n"
                    "State, Country - Pincode",
                },
            ),
            "bio": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super(GeneralDetailsEditForm, self).__init__(*args, **kwargs)
        self.fields["image"].required = False
        self.fields["bio"].required = False


class TechnicalDetailsEditForm(forms.ModelForm):
    class Meta:
        model = TechnicalDetail
        exclude = ["user"]
        widgets = {}

    def __init__(self, *args, **kwargs):
        super(TechnicalDetailsEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False


class TechnicalDetailsExtraURLsEditForm(forms.ModelForm):
    class Meta:
        model = TechnicalDetailsExtraURL
        exclude = ["user"]
        widgets = {}

    def __init__(self, edit=True, *args, **kwargs):
        super(TechnicalDetailsExtraURLsEditForm, self).__init__(*args, **kwargs)
        self.edit = edit


class EducationalDetailsEditForm(forms.ModelForm):
    class Meta:
        model = EducationalDetail
        exclude = ["user"]
        widgets = {}

    def __init__(self, edit=True, *args, **kwargs):
        non_required_fields = [
            "institute_address",
            "year_of_admission",
            "percentage",
            "cgpa",
            "major_subject",
        ]
        super(EducationalDetailsEditForm, self).__init__(*args, **kwargs)
        for field in non_required_fields:
            if field in self.fields:
                self.fields[field].required = False
