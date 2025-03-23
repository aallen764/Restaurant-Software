from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Restaurant Search'
    return render(request, 'search/index.html', {'template_data': template_data})



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
    


