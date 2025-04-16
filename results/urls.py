from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


#test
urlpatterns = [
    path('', views.index, name="results.index"),
    path('', views.get_city_from_zip, name='results.index'),
    path('', views.findRestaurants, name='results.index')
]
