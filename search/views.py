from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import requests
from django.contrib.auth.decorators import login_required
from signUp.models import user_Profile

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        template_data = {}
        template_data['title'] = 'Restaurant Search'

        # pulling user to get their zipcode
        user = request.user

        try:
            user_profile = user.user_profile  # Accessing the user_profile linked to the user
            zip_code = user_profile.zip_code
        except user_Profile.DoesNotExist:
            return HttpResponse("User profile not found.", status=404)
        
        city = get_city_from_zip(zip_code)
        print(city)

        businesses = findRestaurants(city)
        for business in businesses:
            print(business['name'])

        return render(request, 'search/index.html', {'template_data': template_data})
    else:
        return redirect('/')



