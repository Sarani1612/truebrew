from django import forms
from .models import Order


class PaymentForm(forms.Form):
    '''
    Form for inputting payment card details
    '''
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    payment_card_number = forms.CharField(
        label="Payment card number", required=False)
    cvv = forms.CharField(label="Security code (CVV)", required=False)
    expiry_month = forms.ChoiceField(
        label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput())


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'user', 'full_name', 'street_address1',
            'street_address2', 'town_or_city', 'county',
            'postcode', 'country', 'phone_number'
        )
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'Full Name:'
        self.fields['street_address1'].label = 'Street Address:'
        self.fields['street_address2'].label = 'Street Address 2:'
        self.fields['town_or_city'].label = 'Town/City:'
        self.fields['county'].label = 'County/State:'
        self.fields['postcode'].label = 'Postcode:'
        self.fields['country'].label = 'Country:'
        self.fields['phone_number'].label = 'Phone Number:'
