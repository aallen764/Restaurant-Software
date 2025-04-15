from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="account.index"),
    path('update/', views.update_account, name="account.update"),
    path('change-password/', views.change_password_page, name='account.password_form'),
    path('change-password/submit/', views.change_password, name='account.password_submit'),
]
