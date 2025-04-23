from django.shortcuts import render, redirect # use redirect to send user to login page after 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.views import generic
from .forms import login_Form

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated: # functionality if user is NOT logged in when view is called
        if request.method == "POST":
            return user_Login(request)
        else:
            template_data = {}
            template_data['title'] = 'BiteFinder'
            
            if 'error_message' in request.session:
                del request.session['error_message']
                
            return render(request, 'login/login2.html', {'template_data': template_data})
    else: # if user IS logged in, redirect back to homepage (they shouldn't be able to access this page)
        return(redirect('/'))
    
def user_Login(request):
    if request.method == "POST":
        error_profile = login_Form(request.POST)
        if error_profile.is_valid():
            username = error_profile.cleaned_data["username"]
            password = error_profile.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                auth_login(request, user)
                return redirect('/') # redirect to homepage after successfully logging in
    else:
        error_profile = login_Form()
    
    return render(request, 'login/login2.html', {'error_profile': error_profile})

def logout_view(request):
    if request.user.is_authenticated: # if user is logged in, allow them to log out
        logout(request)
        return redirect('/') # redirect to homepage after signing out
    else: # if not logged in, they can't logout so return to homepage
        return redirect('/')
