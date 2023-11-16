from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    # note: we intentionally assume POST data is valid
    def clean(self):
        data = super().clean()
        if data.get('password1') != data.get('password2'):
            raise ValidationError("Passwords don't match")
        return data
