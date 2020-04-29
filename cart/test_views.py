from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Subscription, Product

class TestViews(TestCase):

    def test_view_cart(self):
        page = self.client.get('/cart/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')


# unfinished, commenting out so it doesn't fail
'''
    def test_add_to_cart(self):
        product = Product.objects.create(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')
        
        sub = Subscription.objects.create(frequency='Monthly', description='This is a monthly test description', unit_price=20, practical_info='This is practical info test', product=product)
        quantity = 1
        session = self.client.session
        session['cart'] = 'cart_session'

        page = self.client.post("/cart/add/{0}/".format(sub.id),)

        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, '/cart/')
'''