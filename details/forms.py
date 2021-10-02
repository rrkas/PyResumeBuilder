import django.forms as forms

from details.models import GeneralDetails, TechnicalDetails, TechnicalDetailsExtraURL


class GeneralDetailsEditForm(forms.ModelForm):
    class Meta:
        model = GeneralDetails
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
        model = TechnicalDetails
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
