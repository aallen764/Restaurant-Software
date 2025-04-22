import requests
from django.conf import settings

YELP_API_URL = "https://api.yelp.com/v3/businesses/search"

def search_restaurants(term, location, categories=None, open_now=None, limit=4):
    headers = {
        "Authorization": f"Bearer {settings.YELP_API_KEY}"
    }

    # Parse coordinates (latitude,longitude)
    
    latitude, longitude = location.split(',')
    params = {
        "term": term,
        "latitude": latitude,
        "longitude": longitude,
        "limit": limit
    }
    
    # Add optional filters only if they are not None
    if categories:
        params["categories"] = categories
    if open_now:
        params["open_now"] = open_now
    
    
    # Send request to Yelp API
    response = requests.get(YELP_API_URL, headers=headers, params=params)
    
    
    
    # Check response status
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}