from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from accounts.models import UserInfo
from .models import OrderLineItem
from .forms import OrderForm
from django.utils import timezone
import stripe
from products.models import Product, Subscription


stripe_publishable = settings.STRIPE_PUBLISHABLE
stripe.api_key = settings.STRIPE_API_KEY

# Create your views here.
@login_required()
def checkout(request):
    if request.method == 'POST':
        token = request.POST['stripeToken']
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            subtotal = 0
            for id, quantity in cart.items():
                subscription = get_object_or_404(Subscription, pk=id)
                subscription_total = quantity * subscription.unit_price
                subtotal += subscription_total
                order_line_item = OrderLineItem(
                    order=order,
                    subscription=subscription,
                    quantity=quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(subtotal*100),
                    currency="EUR",
                    description=request.user.email,
                    source=token,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "Thank you, your order has been placed!")
                request.session['cart'] = {}
                return redirect('account')
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(order_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
    else:
        try:
            UserInfo.objects.get(user=request.user)
            initial = {
                'user': request.user.id,
                'full_name': request.user.first_name + ' ' + request.user.last_name,
                'street_address1': request.user.userinfo.street_address1,
                'street_address2': request.user.userinfo.street_address2,
                'town_or_city': request.user.userinfo.town_or_city,
                'county': request.user.userinfo.county,
                'postcode': request.user.userinfo.postcode,
                'country': request.user.userinfo.country,
                'email': request.user.email,
                'phone_number': request.user.userinfo.phone_number
            }
        except UserInfo.DoesNotExist:
            initial = {
                'user': request.user.id
            }
        order_form = OrderForm(request.POST or None, initial=initial)
    context = {
        'order_form': order_form,
        'stripe_publishable': stripe_publishable
    }
    return render(request, "checkout.html", context)
