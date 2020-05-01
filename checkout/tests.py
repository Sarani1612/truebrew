from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class TestViews(TestCase):
    '''
    tests that users not logged in are rerouted to login page
    '''
    def test_checkout_reroute_for_guests(self):
        page = self.client.get('/checkout/')

        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, '/accounts/login/?next=/checkout/')

    def test_checkout_page(self):
        testuser = User.objects.create_user(username='johnsmith', email='john@smith.com', password='Teapot486')
        self.client.login(username='johnsmith', password='Teapot486')

        page = self.client.get('/checkout/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'checkout.html')
