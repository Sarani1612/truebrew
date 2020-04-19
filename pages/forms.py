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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email Address:'
        self.fields['title'].label = 'Subject Line:'
        self.fields['message_body'].label = 'Message:'
