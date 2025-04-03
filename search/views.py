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



# This converts the zipcode, which we will pull from the signed in user to a city name
def get_city_from_zip(zip_code):
    api_key = 'sDHNgJQ5B8UKDM9Sl5vNe158RvwjPcryLiKWY1UGgnkiiMSk5Z2iLkGuoAoaBjFt'
    url = f'https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'
    response = requests.get(url)
    data = response.json()
    return data.get('city', 'City not found')


def findRestaurants(city):
    API_KEY = '8IsAViZ9EV4sgczPyama_sNAMtRagiWIQk1nU6QdQA6QJ5iR3L9Exd-fBXkOKVQHQW93gySAvGrNyzTBz0C7UA0lX1Z__z_PLLkVug3hb2vSrH4VguGtHhC9T1HTZ3Yx'
    HEADERS = {'Authorization': f'Bearer {API_KEY}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'term': 'restaurant',
        'location': city,
        'categories': 'restaurants',
        'limit': 4,
        'radius': 10000
    }
    response=requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        businesses = data['businesses']
        return businesses
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
