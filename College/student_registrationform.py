from django import forms
from django.contrib.auth.models import User

from .models import StudentRegistration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        exclude = ["name", "user"]


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
