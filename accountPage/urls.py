from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="account.index"),
    path('update/', views.update_account, name="account.update"),
]