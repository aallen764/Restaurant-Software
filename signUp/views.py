from django.shortcuts import render, redirect # use redirect to send user to login page after 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import generic
from django.template import loader
from .models import user_Profile
from .forms import registration_Form, profile_Form

# Create your views here.
def signUp(request): # view for sign_up
    if not request.user.is_authenticated: # if user is NOT logged in, allow them to continue with sign-up view/process
        if request.method == "POST":
            return user_Register(request)
        else:
            template_data = {}
            template_data['title'] = 'BiteFinder'
            return render(request, 'signUp/register2.html', {'template_data': template_data})
    else: # if user is NOT logged in, they can't sign up, so redirect them back to homepage
        return redirect('/')

def user_Register(request):
    if request.method == "POST":
        user_form = registration_Form(request.POST)
        profile_form = profile_Form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"]) # hides inputted password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user # connects profile object to user object
            profile.save()

            login(request, user)
            return redirect("/")
    else:
        user_form = registration_Form()
        profile_form = profile_Form()
    
    return render(request, 'signUp/register2.html', {"user_form": user_form, "profile_form": profile_form})