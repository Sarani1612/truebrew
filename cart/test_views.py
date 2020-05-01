from django.test import TestCase, Client
from django.contrib.auth.models import User
from products.models import Subscription, Product

class TestViews(TestCase):

    def test_view_cart(self):
        '''
        Tests the cart view when there are no items in the cart
        '''
        page = self.client.get('/cart/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        self.assertContains(page, 'There are no items in your cart yet.')


class TestAddAndAdjust(TestCase):
    def setUp(self):
        self.product = Product.objects.create(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')
        
        self.sub = Subscription.objects.create(frequency='Monthly', description='This is a monthly test description', unit_price=20, practical_info='This is practical info test', product=self.product)

    def tearDown(self):
        self.product.delete()
        self.sub.delete()


    def test_add_to_cart(self):
        '''
        Tests adding product to cart and rendering the cart view
        '''
        sub = self.sub
        session = self.client.session
        session['cart'] = 'cart'

        page = self.client.post("/cart/add/{0}/".format(sub.id), {'quantity': 1})

        response = self.client.get('/cart/')

        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, '/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<table class="w-100">')

    def test_adjust_amount_in_cart(self):
        '''
        Tests correct response to adjusting amounts in cart
        '''
        sub = self.sub
        session = self.client.session
        session['cart'] = 'cart'

        response = self.client.post("/cart/adjust/{0}/".format(sub.id), {'quantity': 3})

        page = self.client.get('/cart/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')
        self.assertEqual(page.status_code, 200)
