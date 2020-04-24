import os
from .models import Product

def dropdown_products(request):
    products = Product.objects.all().order_by('pk')
    return {'products': products}
