from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView  

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('logout/', LogoutView.as_view(), name='signOut'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)