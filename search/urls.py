from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='search.index'),
    path('', views.get_city_from_zip, name='search.index'),
    path('', views.findRestaurants, name='search.index')
]