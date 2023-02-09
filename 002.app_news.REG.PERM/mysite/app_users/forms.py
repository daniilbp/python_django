from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=36, required=True, help_text='Телефон')
    city = forms.CharField(max_length=36, required=False, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'city', 'password1', 'password2')
