from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    '''Form to create a user account'''
    email = forms.EmailField(label='Enter your email address:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Enter a username:'
        self.fields['password1'].label = 'Enter a password:'
        self.fields['password2'].label = 'Enter the password again:'


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'username:'
        self.fields['email'].label = 'Email Address:'
        self.fields['first_name'].label = 'First Name:'
        self.fields['last_name'].label = 'Last Name:'


class EditUserInfoForm(ModelForm):
    ''' Form to be used by a user in order to edit their account details '''
    class Meta:
        model = UserInfo
        fields = ['street_address1', 'street_address2', 'town_or_city',
                  'postcode', 'county', 'country', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street_address1'].label = 'Street Address:'
        self.fields['street_address2'].label = 'Street Address 2:'
        self.fields['town_or_city'].label = 'Town/City:'
        self.fields['postcode'].label = 'Postcode:'
        self.fields['county'].label = 'County/State:'
        self.fields['country'].label = 'Country:'
        self.fields['phone_number'].label = 'Phone Number:'
