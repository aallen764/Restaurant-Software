from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register2/', views.RegistrationView, name="register"),
    path('login2/', views.LoginView, name="userLogin"),
    path('test/', views.test, name="test"),
]