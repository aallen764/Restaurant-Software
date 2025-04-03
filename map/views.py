from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View


# Create your views here.
class MapView(View):
    
    template_name = "map/index.html"

    def get(self, request):
        if request.user.is_authenticated:
            key = 'AIzaSyAREHr_JNo0KmsVoRgcKSU9t_vqk1mz0No'
            context = { 
                "key":key
            }
            return render(request, self.template_name, context)
        else:
            return redirect('/')