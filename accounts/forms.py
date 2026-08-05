from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254 , required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangePasswordForm(forms.Form):
    username_or_email = forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput)
    