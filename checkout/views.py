from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import OrderLineItem
from .forms import PaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
import stripe
from products.models import Product, Subscription

# gets products to populate navbar dropdown in all views
products = Product.objects.all()

# Create your views here.
@login_required()
def checkout(request):
    context = {
        'products': products,
        # 'order_form': order_form,
        # 'payment_form': payment_form,
        # 'publishable': settings.STRIPE_PUBLISHABLE
        }
    return render(request, "checkout.html", context)
