from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="account.index"),
    path('update/', views.update_account, name="account.update"),
    path('change-password/submit/', views.change_password, name='account.password_submit'),
]
