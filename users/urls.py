from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegistrationView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('test/', views.test, name="test"),
]