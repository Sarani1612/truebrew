from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    '''Form to create a user account'''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(UserChangeForm):
    '''
    Ensures 'password' does not show up in the form,
    as it cannot be changed there.
    Solution found at https://stackoverflow.com/questions/16337349/exclude-username-or-password-from-userchangeform-in-django-auth
    '''
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class EditUserInfoForm(ModelForm):
    ''' Form to be used by a user in order to edit their account details '''
    class Meta:
        model = UserInfo
        fields = ['street_address1', 'street_address2', 'town_or_city',
                  'postcode', 'county', 'country', 'phone_number']
