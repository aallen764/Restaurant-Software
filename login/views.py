from django.shortcuts import render, redirect # use redirect to send user to login page after 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.views import generic
from django.template import loader

# Create your views here.
def login_view(request):
    if request.method == "POST":
        return user_Login(request)
    else:
        template_data = {}
        template_data['title'] = 'BiteFinder'
        return render(request, 'login/login2.html', {'template_data': template_data})
    
def user_Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "LOGIN WAS SUCCESSFUL")
            return redirect('test')  
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login/login2.html')

def test(request):
    return HttpResponse("IF YOU'RE SEEING THIS, THEN YOU'RE LOGGED IN!")