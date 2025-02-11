from django.shortcuts import render


# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'about/index.html', {'template_data': template_data})
