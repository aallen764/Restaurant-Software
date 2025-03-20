from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login.index'),
    path('test/', views.test, name="test"),
    path('logout/', views.logout_view, name='logout')
]