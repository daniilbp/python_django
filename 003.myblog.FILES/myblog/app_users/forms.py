from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import Profile


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=False, help_text='Name')
    surname = forms.CharField(max_length=20, required=False, help_text='Test!2#4')

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'password1', 'password2')


class UploadAvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)


# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('name', 'surname', 'avatar')
