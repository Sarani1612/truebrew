from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from products.models import Product
from .forms import ContactMessageForm


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def contact_page(request):
    '''
    renders the contact page, and if user is logged in,
    will pre-populate 'user' (hidden field) and 'email'.
    '''
    if request.method == 'POST':
        contact_form = ContactMessageForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()

            email = request.POST['email']
            title = request.POST['title']
            message_body = request.POST['message_body']

            # send email
            send_mail(
                title,
                message_body,
                email,
                ['truebrewboxes@gmail.com']
            )

            messages.success(request,
                'Your message has been sent. Thank you for getting in touch!')
        else:
            messages.error(
                request,
                'Sorry, something went wrong. Please try again.')
        return redirect('contact')

    else:
        if request.user.is_authenticated:
            initial = {
                'user': request.user,
                'email': request.user.email
            }
            contact_form = ContactMessageForm(initial=initial)
        else:
            contact_form = ContactMessageForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'contact.html', context)
