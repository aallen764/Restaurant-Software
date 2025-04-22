from django.shortcuts import render
from django.http import JsonResponse
from .yelp_api import search_restaurants




def restaurant_search(request):
    term = request.GET.get('term', 'food')

    # Check if "Nearby" is checked and coordinates are provided
    nearby = request.GET.get('nearby', 'on')  # Check for 'on' instead of 'true'
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)

    # Determine location
    if nearby and latitude and longitude:
        # Use user's current location (latitude and longitude)
        location = f"{latitude},{longitude}"
    else:
        # Default to Lakeland, FL
        location = '28.0395,-81.9498'

    # Check if "Open Now" is checked
    open_now = request.GET.get('open_now') == 'on'  # Check for 'on'

    # Check if "Bar" is checked, if so set category to 'bars'
    categories = 'bars' if request.GET.get('bar') == 'on' else None  # Check for 'on'

    # Get data from Yelp API
    data = search_restaurants(term, location, categories, open_now)

    # Return results to HTML


# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'BiteFinder'
    return render(request, 'home/index.html', {'template_data': template_data})
    
    
    
    
    