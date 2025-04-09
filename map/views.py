from django.shortcuts import render
from django.conf import settings
from django.views import View
from results.views import findRestaurants
from results.views import get_city_from_zip
import requests


# Create your views here.
class MapView(View):
    template_name = "map/index.html"

    def get(self, request):
        key = 'AIzaSyAREHr_JNo0KmsVoRgcKSU9t_vqk1mz0No'
        context = { 
            "key":key
        }
        return render(request, self.template_name, context)
