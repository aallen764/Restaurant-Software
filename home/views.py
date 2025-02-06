from django.shortcuts import render


# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'BiteFinder'
    return render(request, 'home/index.html', {'template_data': template_data})