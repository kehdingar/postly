from django.urls import path
from .views import UserCreateAPIView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
