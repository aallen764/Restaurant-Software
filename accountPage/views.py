from django.shortcuts import render
from django.http import HttpResponse
from signUp.models import user_Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'account'
    return render(request, 'accountPage/index.html', {'template_data': template_data})

def change_Username(request):
    if request.method == "POST":
        user = request.user  # grab current user
        current_Username = request.user.get_username() # grab username of current user