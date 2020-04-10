from django.shortcuts import render
from products.models import Product


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
