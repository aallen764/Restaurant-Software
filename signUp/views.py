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
def signUp(request):
    if request.user.is_authenticated:
        return redirect('/')

    user_form = registration_Form()
    profile_form = profile_Form()

    if request.method == "POST":
        user_form = registration_Form(request.POST)
        profile_form = profile_Form(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()

            # creates profile automatically with signal call
            profile = user.user_profile  # creates reference variable for the newly created profile
            profile.email_address = profile_form.cleaned_data["email_address"]
            profile.zip_code = profile_form.cleaned_data["zip_code"]
            profile.phone_number = profile_form.cleaned_data["phone_number"]
            profile.save()

            login(request, user)
            return redirect("/")

    return render(request, 'signUp/register2.html', {
        "user_form": user_form, 
        "profile_form": profile_form
    })