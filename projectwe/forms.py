from django import forms
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries


class ProfileEditForm(forms.Form):
    username = forms.CharField(disabled=True, required=False)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    country = LazyTypedChoiceField(choices=countries)

    def send_email(self):
        pass
