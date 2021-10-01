import django.forms as forms

from details.models import GeneralDetails


class GeneralDetailsEditForm(forms.ModelForm):
    class Meta:
        model = GeneralDetails
        exclude = ['user']
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'House/ Plot/ Landmark, Street\n'
                                   'City, District\n'
                                   'State, Country - Pincode'
                },
            ),
            "bio": forms.Textarea(
                attrs={'rows':3}
            )
        }

    def __init__(self, *args, **kwargs):
        super(GeneralDetailsEditForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['bio'].required = False
