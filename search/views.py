from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from django.contrib.auth.decorators import login_required
from signUp.models import user_Profile

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Restaurant Search'

    return render(request, 'search/index.html', {'template_data': template_data})



