from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required
from signUp.models import user_Profile

# The index function to handle the search
@login_required
def index(request):
    template_data = {}
    template_data['title'] = 'Restaurant Search'

    # Get search query from the request
    query = request.GET.get('query', '')  # This gets the 'query' from the URL parameters
    nearby = request.GET.get('nearby', None)  # 'None' means unchecked
    open_now = request.GET.get('open', None)
    bar = request.GET.get('Bar', None)

    # pulling user to get their zipcode
    user = request.user

    try:
        user_profile = user.user_profile  # Accessing the user_profile linked to the user
        zip_code = user_profile.zip_code
    except user_Profile.DoesNotExist:
        return HttpResponse("User profile not found.", status=404)
    
    city = get_city_from_zip(zip_code)  # Convert zip code to city

    # Find restaurants based on the city and search query (if provided)
    businesses = findRestaurants(city, query, nearby, open_now, bar)  # Pass the search query to findRestaurants

    return render(request, 'results/index.html', {'template_data': template_data, 'businesses': businesses})


# Function to convert zipcode to city
def get_city_from_zip(zip_code):
    api_key = 'sDHNgJQ5B8UKDM9Sl5vNe158RvwjPcryLiKWY1UGgnkiiMSk5Z2iLkGuoAoaBjFt'
    url = f'https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'
    
    try:
        response = requests.get(url)
        data = response.json()
        city = data.get('city', 'Lakeland')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        city = 'Lakeland'
    except ValueError as e:
        print(f"Invalid JSON response: {e}")
        city = 'Lakeland'
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        city = 'Lakeland'
    
    return city


# Function to search restaurants using Yelp API based on city and query
def findRestaurants(city, query, nearby, open_now, bar):
    API_KEY = '8IsAViZ9EV4sgczPyama_sNAMtRagiWIQk1nU6QdQA6QJ5iR3L9Exd-fBXkOKVQHQW93gySAvGrNyzTBz0C7UA0lX1Z__z_PLLkVug3hb2vSrH4VguGtHhC9T1HTZ3Yx'
    HEADERS = {'Authorization': f'Bearer {API_KEY}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    
    params = {
        'term': query if query else 'restaurant',  # Use query if available, else default to 'restaurant'
        'location': city,
        'categories': 'restaurants',
        'limit': 10,
        'radius': 10000
    }

    if nearby:
        params['sort_by'] = 'distance'  # Example: Sort by distance for nearby
    if open_now:
        params['open_now'] = True
    if bar:
        params['categories'] = 'bars'
    
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        businesses = data['businesses']
        return businesses
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []
