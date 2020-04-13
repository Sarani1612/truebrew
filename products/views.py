from django.shortcuts import render, get_object_or_404
from .models import Product

# gets products to populate navbar dropdown in all views
products = Product.objects.all()


def view_product(request, pk):
    tea = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {'product': tea, 'products': products})
