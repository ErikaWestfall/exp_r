from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(required=False)
    lastName = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstName = forms.CharField(required=False)
    lastName = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'twitter', 'linkedin', 'facebook', 'github', 'image', 'bio',]