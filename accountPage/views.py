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

def index2(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    # call the signup forms for user & profile form to check if new user information is valid (clean)
    # if input field is EMPTY -> set equal to default value
    #
    # change to a ONE-PAGE system - -> add bootstrap image (pencil) next to each user info field
    # clickable button creates text field and calls signup clean-up forms to check validity