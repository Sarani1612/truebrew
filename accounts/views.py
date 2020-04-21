from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, EditUserInfoForm, EditUserForm
from .models import UserInfo
from products.models import Product

# gets products to populate navbar dropdown in all views
products = Product.objects.all()


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
        else:
            messages.error(request, 'Login failed - please try again', extra_tags='danger')
            return redirect('login')
    else:
        return render(request, 'login.html', {'products': products})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully created an account!")
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form, 'products': products})


@login_required
def user_account(request):
    '''The users profile page'''
    return render(request, 'account.html', {'products': products})


@login_required
def edit_account(request):
    '''
    Renders a form for the user to fill out with contact details.
    If the user already has info stored, the form will be pre-populated.
    If not, a new UserInfo object will be created.
    '''
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        user_info_form = EditUserInfoForm(request.POST, instance=request.user.userinfo)
        if user_form.is_valid() and user_info_form.is_valid():
            user_form.save()
            user_info_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('account')
        else:
            messages.error(request, 'Your form has errors', extra_tags='danger')
    else:
        obj, created = UserInfo.objects.get_or_create(user=request.user)
        initial = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'street_address1': request.user.userinfo.street_address1,
            'street_address2': request.user.userinfo.street_address2,
            'town_or_city': request.user.userinfo.town_or_city,
            'county': request.user.userinfo.county,
            'postcode': request.user.userinfo.postcode,
            'country': request.user.userinfo.country,
            'email': request.user.email,
            'phone_number': request.user.userinfo.phone_number
        }
        user_form = EditUserForm(request.POST or None, initial=initial)
        user_info_form = EditUserInfoForm(request.POST or None, initial=initial)
        context = {
            'products': products,
            'user_form': user_form,
            'user_info_form': user_info_form
            }
        return render(request, 'editaccount.html', context)
