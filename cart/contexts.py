from django.shortcuts import get_object_or_404
from products.models import Subscription


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []
    subtotal = 0
    subscription_count = 0

    for id, quantity in cart.items():
        subscription = get_object_or_404(Subscription, pk=id)
        subscription_total = quantity * subscription.unit_price
        subtotal += subscription_total
        subscription_count += quantity
        cart_items.append({
            'id': id,
            'quantity': quantity,
            'subscription': subscription,
            'subscription_total': subscription_total
            })

    return {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'subscription_count': subscription_count
        }
