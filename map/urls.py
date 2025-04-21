from django.urls import path, include
from .views import *
from .views import MapView

urlpatterns = [
    path('', MapView.as_view(), name='map.index'),
]