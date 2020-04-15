from django.shortcuts import render
from products.models import Product


# gets products to populate navbar dropdown in all views
products = Product.objects.all()


# Create your views here.
def view_cart(request):
    return render(request, 'cart.html', {'products': products})