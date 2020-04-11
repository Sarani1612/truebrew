from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def user_registration(request):
    return render(request, 'register.html')


@login_required
def user_account(request):
    '''The users profile page'''
    return render(request, 'account.html')
