from django.test import TestCase
from .models import Product, Subscription


# Create your tests here.
class TestModels(TestCase):

    def test_save_product(self):
        '''
        tests that a product gets saved correctly
        '''
        product = Product(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')
        product.save()

        self.assertEqual(product.id, 1)
        self.assertEqual(product.description, 'Long description')
    
    def test_save_subscription(self):
        '''
        tests that a subscription gets saved correctly
        referencing the product it is related to
        '''
        product = Product(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')
        product.save()

        sub = Subscription(frequency='Monthly', description='This is a monthly test description', unit_price=20, practical_info='This is practical info test', product=product)
        sub.save()

        self.assertEqual(sub.frequency, 'Monthly')
        self.assertEqual(sub.product.id, 1)

class TestModelStrings(TestCase):
    '''
    tests that the strings for Product and Subscription models are returned correctly
    '''
    def setUp(self):
        self.product = Product.objects.create(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')
    
        self.sub = Subscription.objects.create(frequency='Monthly', description='This is a monthly test description', unit_price=20, practical_info='This is practical info test', product=self.product)

    def tearDown(self):
        self.product.delete()
        self.sub.delete()


    def test_product_string(self):
        product = self.product

        self.assertEqual(str(product), 'Black Tea')

    def test_subscription_string(self):
        sub = self.sub
        
        self.assertEqual(str(sub), 'Monthly-Black Tea')