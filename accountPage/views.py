from django.shortcuts import render, redirect
from django.http import HttpResponse
from signUp.models import user_Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        template_data = {}
        template_data['title'] = 'account'
        return render(request, 'accountPage/index.html', {'template_data': template_data})
    else:
        return redirect('/')

def change_Username(request):
    if request.method == "POST":
        user = request.user  # grab current user
        current_Username = request.user.get_username() # grab username of current user