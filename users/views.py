from django.shortcuts import render, redirect # use redirect to send user to login page after 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import generic
from django.template import loader

# Create your views here

def RegistrationView(request):
    if request.method == "POST":
        return user_Register(request)
    else:
        return render(request, 'users/register.html')

def LoginView(request):
    if request.method == "POST":
        return user_Login(request)
    else:
        return render(request, 'users/login.html')

def user_Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            login(request, user)
            messages.success(request, "LOGIN WAS SUCCESSFUL")
            return redirect('users:test')
    
    return render(request, "users/register.html")

def user_Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "LOGIN WAS SUCCESSFUL")
            return redirect('users:test')  
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def test(request):
    return HttpResponse("IF YOU'RE SEEING THIS, THEN YOU'RE LOGGED IN!")