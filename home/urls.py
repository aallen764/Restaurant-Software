from django.urls import path
from .import views

#test
urlpatterns = [
    path('', views.index, name="home.index"),
]
