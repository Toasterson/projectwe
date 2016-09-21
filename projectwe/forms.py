from django import forms


class ProfileEditForm(forms.Form):
    username = forms.CharField(disabled=True, required=False)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField()

    def send_email(self):
        pass