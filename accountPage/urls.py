from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="account.index"),
    path('help', views.index2, name="account.index2"),
]