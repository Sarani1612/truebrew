from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    '''
    Form to be used by users to send a message.
    If the user is logged in, the email is pre-populated.
    '''

    class Meta:
        model = ContactMessage
        fields = ['user', 'email', 'title', 'message_body']
        widgets = {'user': forms.HiddenInput()}
