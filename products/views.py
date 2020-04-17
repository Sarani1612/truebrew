from django.shortcuts import render, get_object_or_404
from .models import Product, Subscription

# gets products to populate navbar dropdown in all views
products = Product.objects.all()


def all_products(request):
    ''' renders the allproducts template showing a card for each tea '''
    return render(request, 'allproducts.html', {'products': products})


def view_product(request, pk):
    '''
    product view showing a card for a given tea
    and the available subscriptions
    '''
    tea = get_object_or_404(Product, pk=pk)
    subs = Subscription.objects.filter(
        product__exact=tea).order_by('unit_price')

    context = {
        'product': tea,
        'subscriptions': subs,
        'products': products
    }
    return render(request, "product.html", context)
