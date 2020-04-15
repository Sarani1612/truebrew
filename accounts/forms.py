from django import forms
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class EditUserInfoForm(UserChangeForm):
    class Meta:
        model = UserInfo
        fields = ['street_address1', 'street_address2', 'town_or_city', 'postcode', 'county', 'country', 'phone_number']
