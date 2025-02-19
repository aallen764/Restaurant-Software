from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def signUp(request):
    template_data = {}
    template_data['title'] = 'BiteFinder'
    return render(request, 'signUp/signUp.html', {'template_data': template_data})