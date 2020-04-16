from django.shortcuts import render, get_object_or_404
from .models import Product

# gets products to populate navbar dropdown in all views
products = Product.objects.all()


def view_product(request, pk):
    tea = get_object_or_404(Product, pk=pk)
    subs = tea.subscriptions.all()

    context = {
        'product': tea,
        'subscriptions': subs,
        'products': products
    }
    return render(request, "product.html", context)
