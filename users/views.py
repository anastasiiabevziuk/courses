from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - LogIn' ,
        'form': form
    }
    return render(request, "users/login.html", context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form 
    }
    return render(request, "users/registration.html", context)


def user_cart(request):
    return render(request, "users/cart.html", )

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Profile',
        'form': form 
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))