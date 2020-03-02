from django import forms
from .models import StaffRegistration
from django.contrib.auth.models import User


class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffRegistration
        exclude = ('user', 'email')


class StaffUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
