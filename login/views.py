from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def login(request):
    template_data = {}
    template_data['title'] = 'BiteFinder'
    return render(request, 'login/myfirst.html', {'template_data': template_data})