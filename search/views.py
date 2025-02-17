from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Restaurant Search'
    return render(request, 'search/index.html', {'template_data': template_data})