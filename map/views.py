from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from results.views import findRestaurants
from results.views import get_city_from_zip
import requests
from json import dumps


# Create your views here.
class MapView(View):
    
    template_name = "map/index.html"

    def get(self, request):
<<<<<<< HEAD
        if request.user.is_authenticated:
            key = 'AIzaSyAREHr_JNo0KmsVoRgcKSU9t_vqk1mz0No'
            context = { 
                "key":key
            }
            return render(request, self.template_name, context)
        else:
            return redirect('/')
=======
        key = 'AIzaSyAREHr_JNo0KmsVoRgcKSU9t_vqk1mz0No'
        businesses = request.session.get('businesses', [])

        businessesJson = dumps(businesses)
        context = { 
            "key":key,
            "businesses": businessesJson
        }
        return render(request, self.template_name, context)

>>>>>>> 0e189a2d33ff738c188f1c76bd51066d8f520197
