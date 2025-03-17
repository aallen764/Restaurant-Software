from django.shortcuts import render, redirect # use redirect to send user to login page after 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.views import generic
from django.template import loader
import time

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated: # functionality if user is NOT logged in when view is called
        if request.method == "POST":
            return user_Login(request)
        else:
            template_data = {}
            template_data['title'] = 'BiteFinder'
            return render(request, 'login/login2.html', {'template_data': template_data})
    else: # if user IS logged in, redirect back to homepage (they shouldn't be able to access this page)
        return(redirect('/'))
    
def user_Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "LOGIN WAS SUCCESSFUL")
            return redirect('/') # redirect to homepage after successfully logging in
        else:
            messages.error(request, "Invalid username or password.")
    
    return redirect('/') # redirect to homepage if successfully logged in

def logout_view(request):
    if request.user.is_authenticated: # if user is logged in, allow them to log out
        logout(request)
        return redirect('/') # redirect to homepage after signing out
    else: # if not logged in, they can't logout so return to homepage
        return redirect('/')

def test(request):
    if request.user.is_authenticated:
        return HttpResponse("THIS IS THE ACCOUNT PAGE!")
    else:
        return redirect('/')