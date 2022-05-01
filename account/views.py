"""Views for the accounts"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.
def user_login(request):
    """Creating the user login view"""
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request,username = clean_data['username'], 
            password = clean_data["password"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request,"account/login.html",{"form":form})
@login_required
def dashboard(request):
    """User, after login"""
    return render(request, "account/dashboard.html",{"section":"dashboard"})
