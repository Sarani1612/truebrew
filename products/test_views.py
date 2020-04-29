from django.test import TestCase
from .models import Product


# Create your tests here.
class TestProductViews(TestCase):
    def test_all_products_view(self):
        page = self.client.get('/products/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'allproducts.html')

    def test_single_product_view(self):
        product = Product.objects.create(title='Black Tea', category='Black Tea', description='Long description', short_description='Short description')

        page = self.client.get('/products/{0}/'.format(product.id))

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'product.html')
        self.assertContains(page, '<h1 class="text-center">Black Tea</h1>')
