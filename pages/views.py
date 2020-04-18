from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product
from .forms import ContactMessageForm

# gets products to populate navbar dropdown in all views
products = Product.objects.all()


# Create your views here.
def home_page(request):
    return render(request, 'index.html', {'products': products})


def contact_page(request):
    '''
    renders the contact page, and if user is logged in,
    will pre-populate 'user' (hidden field) and 'email'.
    '''
    if request.user.is_authenticated:
        initial = {
            'user': request.user,
            'email': request.user.email
        }
        print(initial)
        contact_form = ContactMessageForm(initial=initial)
    else:
        contact_form = ContactMessageForm()
    context = {
        'products': products,
        'contact_form': contact_form
    }
    return render(request, 'contact.html', context)


def send_message(request):
    '''
    saves the message to the ContactMessage database
    '''
    contact_form = ContactMessageForm(request.POST)
    if contact_form.is_valid():
        contact_form.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('contact')
    else:
        messages.error(
            request,
            'Your message was not sent. Please try again.', extra_tags='danger')
        return redirect('contact')
