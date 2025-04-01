from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'account'
    return render(request, 'accountPage/index.html', {'template_data': template_data})
