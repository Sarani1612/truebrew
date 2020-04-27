from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OrderForm


# Create your tests here.
class TestOrderForm(TestCase):
    def setUp(self):
        self.testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
    
    def tearDown(self):
        self.testuser.delete()

    def test_full_order_form(self):
        user = User.objects.get(id=1)
        form = OrderForm({
            'user': user,
            'full_name': 'John Smith',
            'street_address1': '12 Test St',
            'street_address2': 'Apartment 4',
            'town_or_city': 'Test City',
            'county': 'Co Test',
            'postcode': 'A0A 0A0',
            'country': 'Ireland',
            'email': 'john@smith.com',
            'phone_number': '0123456789'
        })
        self.assertTrue(form.is_valid())
